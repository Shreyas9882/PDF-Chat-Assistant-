import os
from flask import Flask, request, jsonify
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Initialize global variables
conversation_chain = None
chat_history = []

def get_pdf_text(pdf_files):
    text = ""
    for pdf_file in pdf_files:
        pdf_reader = PdfReader(pdf_file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    return text_splitter.split_text(text)

def get_vectorstore(text_chunks):
    embeddings = OllamaEmbeddings(model="llama2")
    return FAISS.from_texts(texts=text_chunks, embedding=embeddings)

def initialize_conversation_chain(vectorstore):
    llm = Ollama(model="llama2")
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )

@app.route('/')
def home():
    # Directly serve the index.html file from the same directory
    with open('index.html', 'r') as f:
        return f.read()

@app.route('/upload', methods=['POST'])
def upload_files():
    global conversation_chain, chat_history
    
    if 'files' not in request.files:
        return jsonify({'error': 'No files uploaded'}), 400
    
    pdf_files = request.files.getlist('files')
    if not pdf_files or all(file.filename == '' for file in pdf_files):
        return jsonify({'error': 'No selected files'}), 400

    try:
        raw_text = get_pdf_text(pdf_files)
        text_chunks = get_text_chunks(raw_text)
        vectorstore = get_vectorstore(text_chunks)
        
        conversation_chain = initialize_conversation_chain(vectorstore)
        chat_history = []
        
        return jsonify({'message': f'Processed {len(text_chunks)} chunks from PDF(s)'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/ask', methods=['POST'])
def ask_question():
    global conversation_chain, chat_history
    
    data = request.get_json()
    if not data or 'question' not in data:
        return jsonify({'error': 'No question provided'}), 400
    
    if not conversation_chain:
        return jsonify({'error': 'Please upload PDFs first'}), 400

    try:
        response = conversation_chain({'question': data['question']})
        chat_history = response['chat_history']
        
        return jsonify({
            'answer': response.get('answer', 'No answer found'),
            'history': [{'role': 'user' if i % 2 == 0 else 'bot', 
                        'content': msg.content} 
                       for i, msg in enumerate(chat_history)]
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)