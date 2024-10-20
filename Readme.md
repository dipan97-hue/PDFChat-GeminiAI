## Project--PDFChat-GeminiAI
----

PDFChat-GeminiAI is an intelligent chatbot that allows you to interact with multiple PDF documents using natural language questions. It leverages LangChain’s text-processing capabilities, Google’s Gemini AI for generating conversational responses, and FAISS for efficient document search. This project enables seamless interaction with complex documents by offering precise and accurate responses based on PDF content

## Features
**Multi-PDF Support**: Upload and process multiple PDF documents at once.

**Intelligent Q&A**: Ask questions related to the content of the uploaded PDFs, and receive accurate answers using Google Gemini AI.

**Text Chunking**: Efficiently splits large documents into manageable chunks for better processing.

**FAISS Integration**: Utilizes FAISS for fast similarity search within PDF content.
Conversational Responses: Generates human-like responses using Google Generative AI, tailored to your specific queries.
Streamlit Interface: Provides a simple and intuitive user interface using Streamlit.
Tech Stack

**LangChain**: For text processing and building the conversational chain.
Google Gemini AI: To generate embeddings and conversational responses.

**PyPDF2**: For PDF parsing and text extraction.

**FAISS**: For vector search and document similarity.

**Streamlit**: For creating the interactive web application.

## How It Works
---------
**Upload PDFs**: Upload one or more PDF documents using the provided interface.
Text Extraction: The content of each PDF is extracted and split into chunks for efficient processing.

**Vector Store Creation**: The text chunks are embedded using Google Gemini AI and stored in FAISS for fast document retrieval.
Ask Questions: Enter a question related to the content of the PDFs, and the system will search for relevant chunks and generate a response based on the most relevant information.

**Conversational Output**: The system will return a human-like answer, or inform you if the answer is not present in the text.

## Setup and Installation
Requirements--
Python 3.10 or later
Google API Key (for accessing Google Gemini AI)
Installation

1) Clone the Repository

```bash
# Clone the repository
git clone https://github.com/dipan97-hue/PDFChat-GeminiAI.git

```


2) Set up the virtual environment:

```bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```
3) Install the required dependencies:

```bash

pip install -r requirements.txt
```
4) Make API key in env file:

```bash
GOOGLE_API_KEY=your-google-api-key
Running the App
Start the Streamlit app:
```
5) Run the Streamlit app:

```bash
streamlit run app.py
Upload PDF files and ask questions through the web interface.
```

## Usage
------

Upload PDF files via the sidebar.
Ask questions in the text input field related to the uploaded documents.
Wait for the chatbot to respond with relevant answers.

## Contribution
------
Feel free to submit issues, feature requests, or pull requests to improve this project!