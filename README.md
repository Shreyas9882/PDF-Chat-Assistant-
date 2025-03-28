# PDF-Chat-Assistant-
The PDF Chat Assistant is a web application that allows users to upload PDF documents and then ask questions about their content. The system uses natural language processing to understand and answer questions based on the uploaded documents. 


KEY FEATURE INCLUDE
1. PDF document processing and text extraction
2. Text chunking for efficient processing
3. Vector embeddings for semantic understanding
4. Conversational memory for contextual questions
5. Simple web interface for easy interaction

TECHNOLOGY STACK

1. Frontend: HTML, CSS with Tailwind, JavaScript
2. Backend: Flask (Python web framework)
3. NLP Processing: LangChain for document processing and conversation management
                    Ollama for LLM (Large Language Model) capabilities
                   FAISS for efficient vector similarity search
4. PDF Processing: PyPDF2 library

HOW IT WORKS
1. User uploads one or more PDF documents
2. System processes the documents into searchable vectors
3. User asks questions about the document content
4. System finds relevant sections and generates answers
5. Conversation history is maintained for context

WORKING PRINCIPLE
1. You Upload PDFs
2. The system extracts all text from the documents.
3. AI Splits text into manageable chunks.
4. Converts them into "vector embeddings" (numeric representations of meaning).
5. Stores them in a fast-search database (FAISS).
6. You Ask Questions
7. The AI Finds the most relevant text chunks from your files.
8. Uses Ollama’s LLM (Llama 2) to generate a clear, accurate answer.
9. Remembers conversation history for follow-up questions.
10. Responses are grounded in your uploaded files, not generic web knowledge.

<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/99928125-c409-4ee5-b2eb-a008b5227ebc" />
<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/b99abed6-c13c-4799-a00f-52b18a0fa517" />
<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/68b2538c-21ad-4324-9839-7080fcc66499" />
<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/88268baf-090d-43e6-b32e-0eb27ff98ad7" />
<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/a627d5c8-3700-47f1-bf01-952cf3a4a9d6" />
<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/03e704a6-2ca0-4afd-85a4-a264be9fe3af" />
<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/88dd5f38-c063-4661-91a0-319a97817a36" />
<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/a3ed4f87-9dfd-4bb4-a365-153041ffc128" />
<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/01378ecc-efe5-45fb-9ca3-58eeba237f85" />
<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/51e8d185-b691-4cf4-95ea-85e89e773aba" />


