import streamlit as st
from dotenv import load_dotenv
import os
import base64
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
import PyPDF2
from docx import Document
from typing import List

# --- SETUP ---
# Load API key from .env file
load_dotenv()

# Configure the OpenAI model
# Make sure to have your OPENAI_API_KEY in the .env file
if not os.getenv("OPENAI_API_KEY"):
    st.error("OPENAI_API_KEY is not set in your .env file!")
else:
    # Use GPT-4o for its powerful multimodal capabilities
    llm = ChatOpenAI(model="gpt-4o")

st.set_page_config(page_title="DocuMind - Your AI Study Partner", page_icon="🧠", layout="wide")
st.title("🧠 DocuMind: AI Study Partner")

# --- HELPER FUNCTIONS (Text Extraction) ---
def extract_text_from_pdf(file) -> str:
    text = ""
    try:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
    return text

def extract_text_from_docx(file) -> str:
    text = ""
    try:
        doc = Document(file)
        for para in doc.paragraphs:
            text += para.text + "\n"
    except Exception as e:
        st.error(f"Error reading DOCX: {e}")
    return text

def extract_text_from_txt(file) -> str:
    try:
        return file.getvalue().decode("utf-8")
    except Exception as e:
        st.error(f"Error reading TXT: {e}")
        return ""

# --- SIDEBAR FOR CONTENT INPUT ---
with st.sidebar:
    st.header("📚 Your Study Material")
    
    st.subheader("Text Content")
    uploaded_docs = st.file_uploader(
        "Upload documents", 
        type=['pdf', 'docx', 'txt'], 
        accept_multiple_files=True
    )
    pasted_text = st.text_area("Or paste text here", height=150)

    st.subheader("🖼️ Image Content")
    uploaded_image = st.file_uploader(
        "Upload an image", 
        type=['png', 'jpg', 'jpeg']
    )

    if st.button("✅ Process and Use Content", use_container_width=True):
        with st.spinner("Processing your content..."):
            full_text = ""
            if pasted_text:
                full_text += pasted_text + "\n\n"
            for doc in uploaded_docs:
                if doc.type == "application/pdf": full_text += extract_text_from_pdf(doc)
                elif doc.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document": full_text += extract_text_from_docx(doc)
                elif doc.type == "text/plain": full_text += extract_text_from_txt(doc)
            st.session_state.text_context = full_text
            
            if uploaded_image:
                st.session_state.image_bytes = uploaded_image.getvalue()
                st.image(uploaded_image, caption="This image is now in context.")
            
            st.session_state.messages = []
            st.success("Content is ready! Ask your questions in the chat.")

    if "text_context" in st.session_state or "image_bytes" in st.session_state:
        if st.button("🗑️ Clear Current Context", use_container_width=True):
            if "text_context" in st.session_state: del st.session_state.text_context
            if "image_bytes" in st.session_state: del st.session_state.image_bytes
            st.session_state.messages = []
            st.rerun()

# --- MAIN CHAT INTERFACE ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_question := st.chat_input("Ask about your content or start a general conversation..."):
    st.session_state.messages.append({"role": "user", "content": user_question})
    with st.chat_message("user"):
        st.markdown(user_question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # --- DYNAMIC PROMPT CONSTRUCTION FOR OPENAI ---
                system_instruction = "You are DocuMind, a helpful multimodal study assistant. Analyze the provided text and/or image context to answer the user's question accurately. If the answer is not in the provided context, say so."
                
                human_content = []
                
                text_context = st.session_state.get("text_context", "")
                if text_context:
                    human_content.append({"type": "text", "text": f"---TEXT CONTEXT---\n{text_context}\n---END OF TEXT CONTEXT---"})

                image_bytes = st.session_state.get("image_bytes")
                if image_bytes:
                    image_base64 = base64.b64encode(image_bytes).decode()
                    human_content.append({
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}
                    })

                human_content.append({"type": "text", "text": f"My question is: {user_question}"})

                messages = [
                    SystemMessage(content=system_instruction),
                    HumanMessage(content=human_content)
                ]
                
                response = llm.invoke(messages)
                response_text = response.content
                
                st.markdown(response_text)
                st.session_state.messages.append({"role": "assistant", "content": response_text})

            except Exception as e:
                st.error(f"An error occurred: {e}")