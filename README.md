
## **Project Title:**  
AI-Powered PDF-Based Question Answering System using LangChain, Ollama, FAISS, and Flask



## **Objective:**  
To create a document question-answering system where users can upload PDF files, ask questions related to the uploaded content, and receive precise and contextually relevant answers using a Large Language Model (LLM). The system processes the documents into embeddings, stores them in a vector store, and uses semantic search to retrieve relevant information for each user query.



## **Step-by-Step Working Principle:**

### **1. User Uploads PDF Documents**
- The user uploads one or more PDF documents via the `/upload` route in the Flask application.
- These files are read and processed using the `PyPDF2` library to extract raw text content from each page.


### **2. Text Chunking**
- Since LLMs and embedding models work better with manageable text sizes, the raw text is split into smaller chunks using LangChain’s `RecursiveCharacterTextSplitter`.
- Each chunk is typically limited to a defined character length (e.g., 1500 characters) with some overlap to preserve context across boundaries.



### **3. Text Embedding**
- Every chunk of text is passed to an embedding model (`OllamaEmbeddings` using the `llama2` model).
- Embeddings are numeric vector representations of text that capture its semantic meaning.
- These embeddings are created for each text chunk and stored in a vector database (FAISS in this implementation).



### **4. Vector Store Creation (Knowledge Base)**
- FAISS (Facebook AI Similarity Search) is used to index and store the embeddings.
- Each embedding vector is associated with its corresponding text chunk so that it can be retrieved later based on similarity to a query.

*Note: The diagram references Pinecone as a scalable vector store. In this implementation, FAISS is used, but the system can be adapted to use Pinecone for production-grade persistence and scaling.*



### **5. Question Asking and Embedding**
- When the user submits a question through the `/ask` route, the system first converts the question into an embedding using the same `OllamaEmbeddings` model.
- This ensures both the document chunks and the question exist in the same vector space for comparison.



### **6. Semantic Search and Retrieval**
- A semantic search is performed in the FAISS vector store using the question embedding.
- FAISS retrieves the top-k most relevant chunks whose embeddings are closest (by cosine similarity or inner product) to the query embedding.
- These top-ranked text chunks are considered the most relevant context for answering the question.



### **7. Prompt Construction**
- The retrieved chunks are formatted into a custom prompt template.
- The prompt includes:
  - A system message guiding the LLM to answer like a domain expert.
  - The retrieved context from the documents.
  - The user’s question.



### **8. Answer Generation using LLM**
- The constructed prompt is sent to the Ollama LLM (specifically using the `llama2` model).
- The LLM generates a context-aware answer based solely on the information present in the prompt, i.e., the relevant document chunks.
- The result is returned to the user and stored in memory for chat history.



### **9. Memory Handling for Conversation Context**
- The system uses `ConversationBufferMemory` from LangChain to retain past interactions.
- This enables multi-turn dialogue, where follow-up questions can refer to earlier ones, and the system maintains context.



### **10. Summarization**
- During the document upload process, the system generates a summary of the document using the LLM.
- This summary can be used as an additional system prompt or metadata to improve understanding or guide future queries.


### **11. Exporting Q&A as CSV**
- The application provides an option to export the full conversation as a CSV file.
- This is handled through `/generate_csv` and `/download` routes.
- Each row of the CSV file contains a question and its corresponding answer.


## **System Architecture Recap (as per the diagram)**

1. **PDF Documents** → Extracted and chunked.
2. **Chunked Text** → Embedded using Ollama and stored in vector store (FAISS/Pinecone).
3. **User Question** → Converted to embedding → Semantic search on vector store.
4. **Top Relevant Chunks** → Used in prompt sent to LLM.
5. **LLM Output** → Answer generated and returned to the user.



## **Core Technologies Used**

| Function                       | Tool / Library             |
|-------------------------------|----------------------------|
| Backend Framework             | Flask                      |
| PDF Parsing                   | PyPDF2                     |
| Text Chunking                 | LangChain - RecursiveCharacterTextSplitter |
| Embeddings                    | OllamaEmbeddings (llama2)  |
| Vector Search                 | FAISS                      |
| Language Model                | Ollama (llama2)            |
| Memory Management             | LangChain ConversationBufferMemory |
| Prompt Engineering            | LangChain PromptTemplate   |
| File Export                   | Python CSV module          |

---

## **Advantages of This Approach**
- Supports domain-specific question answering.
- Provides a private, controllable LLM interface using local models like LLaMA2.
- Uses efficient semantic search rather than brute-force keyword matching.
- Easily extendable to use cloud vector stores like Pinecone.
- Flexible and lightweight, can be containerized or deployed as a web API.


Let me know if you would like a frontend UI designed for this or a complete deployment plan using Docker or cloud services.
