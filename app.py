import streamlit as st  # type: ignore
from PyPDF2 import PdfReader  # type: ignore
from langchain.text_splitter import RecursiveCharacterTextSplitter  # type: ignore
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI  # import both together
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import io

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_PDF_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        try:
            pdf_reader = PdfReader(io.BytesIO(pdf.read()))  # Read the uploaded PDF file
            if pdf_reader.pages:
                for page in pdf_reader.pages:
                    page_text = page.extract_text()  # Extract text from each page
                    if page_text:  # Only add non-empty text
                        text += page_text
            else:
                print(f"No pages found in the PDF: {pdf.name}")
        except Exception as e:
            print(f"Error in reading the PDF {pdf.name}: {e}")  # Log the error message
    return text

def get_chunks(text):
    if not text:  # Check for empty text
        return []
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    if not text_chunks:  # Ensure there are chunks to process
        print("No text chunks to process.")
        return
    embeddings = GoogleGenerativeAIEmbeddings(model='models/embedding-001')
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

def get_conversational_chain():
    prompt_template = """
    Answer the provided question and if the answer is not present in the text please say that the answer is not present in the text. 
    Don't provide wrong answers.\n\n 
    Context:\n{context}?\n
    Question:\n{question}\n

    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)

    # Use the correct initialization of PromptTemplate
    prompt = PromptTemplate(template=prompt_template, input_variables=['context', 'question'])
    chain = load_qa_chain(llm=model, chain_type="stuff", prompt=prompt)
    return chain

def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model='models/embedding-001')
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)
    
    if not docs:  # Check if any documents are found
        st.write("No relevant documents found for the query.")
        return

    chain = get_conversational_chain()
    
    response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)
    
    # Displaying the response to the user
    st.write("Reply:", response["output_text"])

def main():
    st.set_page_config("Chat with Multiple PDF")
    st.header("Chat with Multiple PDF using GEMINI")

    user_question = st.text_input("Ask a question from the PDF uploaded")

    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF(s) and click on the submit to process", type=["pdf"], accept_multiple_files=True)
        if st.button("Submit and Process"):
            if pdf_docs:
                with st.spinner("Processing..."):
                    text = get_PDF_text(pdf_docs)
                    if not text:
                        st.error("No text extracted from the PDFs.")
                        return
                    chunks = get_chunks(text)
                    get_vector_store(chunks)
                    st.success("Processing Done")
            else:
                st.error("Please upload at least one PDF.")

if __name__ == "__main__":
    main()
