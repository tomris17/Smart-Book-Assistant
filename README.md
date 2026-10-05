# Smart Book Assistant Agent

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue.svg)](https://www.python.org/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-VectorSearch-orange.svg)](https://www.trychroma.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)

This project builds an intelligent book assistant agent that uses ChromaDB for retrieval and Gemini models as the autonomous brain to answer user queries and recommend books[cite: 19].

---

## Project Workflow
1. **Database Connection**: Initializing persistent ChromaDB client and accessing the `book_collection` library repository[cite: 19].
2. **Semantic Retrieval**: Querying the vector database to fetch relevant book descriptions, authors, ratings, and summaries based on user requests[cite: 19].
3. **AI Literary Expert Reasoning**: Using Google GenAI and Gemini models with specialized prompt engineering to generate professional and structured book recommendations[cite: 19].
4. **Web Application**: Interactive deployment interface built with Streamlit.

---

## Getting Started & Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/smart-book-assistant.git](https://github.com/YOUR_USERNAME/smart-book-assistant.git)
   cd smart-book-assistant
