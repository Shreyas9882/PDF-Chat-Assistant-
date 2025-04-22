## **Project Title**  
**AI-Powered PDF Question Answering System Using LangChain, Ollama, and Vector Search**


## **Project Description**

This project is a backend web application that enables intelligent question-answering from scientific or research-based PDF documents. The system extracts textual data from PDFs, breaks the content into smaller manageable parts, encodes it into high-dimensional embeddings, and stores them in a searchable vector database. When a user poses a question, the system retrieves the most semantically relevant parts of the document using similarity search and passes this context to a domain-aware language model to generate precise and factual answers.

The solution is ideal for use cases where users need to interact with large documents like research papers, legal documents, medical files, or technical manuals, asking specific questions and receiving accurate, contextual answers without having to read the entire document manually.


## **System Objective**

The goal of the system is to:
- Allow users to upload one or more PDF files.
- Enable automatic extraction and intelligent indexing of document content.
- Facilitate natural language interaction through questions posed by users.
- Provide precise and relevant answers by leveraging an AI model and vector search technology.
- Maintain a history of user interactions for conversational context.
- Enable the export of the question-answer history to a CSV file for offline review or sharing.


## **Key Components and Workflow**

### **1. PDF Upload and Text Extraction**
- The system provides a route (`/upload`) where users can upload PDF files.
- Each file is read page by page using the `PyPDF2` library.
- All extracted text is concatenated into a single text blob representing the document content.

### **2. Text Chunking**
- To make the content manageable for embedding and vector storage, the large text is divided into smaller overlapping segments (chunks).
- The chunking is performed using LangChain’s `RecursiveCharacterTextSplitter`.
- Chunk size and overlap parameters (e.g., 1500 characters with 200-character overlap) ensure each chunk preserves context and coherence.

### **3. Text Embedding and Vector Indexing**
- Each chunk is transformed into a vector representation (embedding) using `OllamaEmbeddings`, which internally uses the `llama2` model.
- These embeddings capture the semantic meaning of the text.
- The resulting vectors are stored in a FAISS vector database for similarity-based retrieval.
- Each embedding is linked to its corresponding chunk, enabling retrieval of relevant document content later.

### **4. Document Summarization**
- Once the text is chunked and embedded, a document-level summary is generated using the Ollama LLM.
- This summary provides a concise overview and is stored for use in prompt generation or display purposes.
- The summary improves prompt conditioning, especially when working with large documents.

### **5. Conversational Retrieval Chain Initialization**
- LangChain’s `ConversationalRetrievalChain` is used to establish an interactive question-answering interface.
- This chain combines:
  - A language model (`llama2`)
  - A vector retriever (FAISS)
  - A conversational memory buffer (`ConversationBufferMemory`)
- The chain is initialized with the generated summary and designed prompts to answer questions based solely on the content of the uploaded document.

### **6. User Question Handling**
- The user sends a question via the `/ask` route.
- The system ensures the question is valid and uses the conversational retrieval chain to process it.
- Steps involved:
  - Embed the question using the same embedding model.
  - Retrieve the top-k most similar document chunks from the FAISS store.
  - Construct a domain-specific prompt that includes the retrieved context and the user’s question.
  - Pass the prompt to the LLM for answer generation.
- The response is stored in `chat_history` for future conversational reference and returned to the user.

### **7. Multi-turn Dialogue Support**
- The use of `ConversationBufferMemory` allows the application to remember previous interactions.
- This enables follow-up questions that refer to earlier responses, creating a fluid and intelligent conversational flow.

### **8. CSV Export Functionality**
- The system provides an endpoint (`/generate_csv`) where a list of questions can be batch-processed.
- For each question, the system uses the same LLM-powered chain to generate answers.
- The results are written into a CSV file, with each row containing a question and its corresponding answer.
- This CSV file can be downloaded using the `/download/<filename>` endpoint.


## **Technology Stack**

| Function                      | Technology / Library                 |
|-------------------------------|--------------------------------------|
| Web Framework                 | Flask (Python)                       |
| PDF Parsing                   | PyPDF2                               |
| Language Model (LLM)          | Ollama (LLaMA2 model)                |
| Text Chunking                 | LangChain `RecursiveCharacterTextSplitter` |
| Embedding Model               | OllamaEmbeddings                     |
| Vector Store                  | FAISS (can be replaced with Pinecone)|
| Prompt Engineering            | LangChain PromptTemplate             |
| Retrieval & Answering         | LangChain ConversationalRetrievalChain |
| Memory for Conversations      | LangChain ConversationBufferMemory   |
| CSV Generation                | Python CSV module                    |
| Frontend Template             | HTML via Flask `render_template`     |


## **Security and Performance Considerations**
- The application assumes local use and has minimal input validation; additional input sanitization and user authentication would be needed for production deployment.
- Embedding and model inference are performed using local models, which is ideal for privacy but may require hardware optimization.
- FAISS is fast and lightweight but lacks persistence. Pinecone or similar cloud-based vector stores should be used for scalable, persistent deployments.


## **Key Features**
- Upload and process multiple PDF documents at once.
- Automatically chunk and embed large documents for efficient retrieval.
- Ask questions in natural language and get fact-based answers grounded in the uploaded content.
- Maintain conversational memory for multi-turn interactions.
- Export question-answer sessions to CSV.
- Configurable to use either local or cloud-based vector databases (FAISS or Pinecone).
- Modular and extensible design using LangChain and Flask.

<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/de48f4a4-6eab-49f4-ad88-0896dec928d6" />
<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/f3341898-4bbc-443d-a990-5888f8f66abc" />
<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/77d1d426-38e3-4d94-82ea-edc8cd86280d" />
<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/fa00f23d-3a76-4794-947c-6ad74efd1563" />
<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/fa394543-57bc-4d08-8dbc-8d3ca13a55d5" />
<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/0b84f236-f172-415a-ae29-3a28af419fbc" />
<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/fd39c84a-9097-47a3-86a4-3bcb7d76568d" />
