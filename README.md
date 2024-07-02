Medical Code Chatbot
Overview
The Medical Code Chatbot is a Streamlit application designed to help users find information about medical codes from uploaded PDF documents. Users can interact with the chatbot by asking questions, and the chatbot will generate answers based on the content of the provided documents.

Features
User-Friendly Interface: Simple and clean interface to interact with the chatbot.
PDF Upload: Upload multiple PDF files for the chatbot to reference.
Text Input: Ask questions directly through a text input box.
Answers Display: The chatbot generates answers based on the uploaded PDFs and displays them on the interface.

Requirements :
Python 3.7 or higher
Streamlit
langchain_community
langchain
FAISS
HuggingFace
PyPDFLoader

Installation :
Clone the repository:
git clone https://github.com/your-repository/medicalchatbot.git
cd medicalchatbot

Install dependencies:
pip install -r requirements.txt

Run the application:
streamlit run medicalchatbot.py

Usage :
Upload PDF files: Use the sidebar to upload one or more PDF files containing medical codes.
Ask a Question: Type your question in the text input box in the main interface.
Get Answers: The chatbot will process the question and display the answer based on the content of the uploaded PDFs.
File Description
medicalchatbot.py: The main script containing the Streamlit application and logic for handling user interactions, PDF uploads, and question answering.
Key Components
Streamlit: Used for building the web application interface.
LangChain: Provides the necessary tools for creating a language model and handling the chatbot logic.
FAISS: A library for efficient similarity search and clustering of dense vectors, used for creating a vector store of the PDF content.
HuggingFace: Used for generating embeddings from the text content of the PDFs.
PyPDFLoader: For loading and processing PDF files.
Detailed Explanation
Streamlit Configuration
The application is configured with a custom page title, icon, and layout settings. Custom CSS styles are used to enhance the appearance of the interface.

PDF Upload and Processing
PDF files can be uploaded through the sidebar. The files are temporarily stored and processed to extract text content. The text is split into manageable chunks and converted into embeddings using HuggingFace models.

Language Model
The application uses a language model from the langchain_community package, specifically LlamaCpp. The model is loaded and used to generate responses based on the provided PDF content and user questions.

Question Answering
When a user asks a question, the application retrieves relevant information from the PDF vector store and generates an answer using a predefined prompt template. The answer is then displayed in the interface.

License
This project is licensed under the MIT License.

Acknowledgements
Streamlit
LangChain
FAISS
HuggingFace
PyPDFLoader
Contact
For any questions or suggestions, please contact daneshdeepan@gmail.com.
