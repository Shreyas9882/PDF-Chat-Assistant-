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

