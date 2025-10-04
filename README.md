# 🧠 DocuMind: AI Study Partner

**DocuMind** is a powerful, multimodal AI study assistant built using Streamlit and OpenAI’s GPT models. It allows students, researchers, and lifelong learners to upload text, documents, and images and interactively ask questions, summarize, or extract key insights from their study materials.

![DocuMind Banner](https://placehold.co/1200x300?text=DocuMind+-+AI+Study+Partner)

---

## 🚀 Features

### **1. Multimodal Input Support**

* Upload **PDF**, **DOCX**, or **TXT** files and automatically extract text.
* Paste text directly for quick use.
* Upload images for multimodal understanding and Q&A.

### **2. AI-Powered Assistance**

* Powered by **GPT-4o**, capable of understanding both text and images.
* Answers questions based on uploaded content.
* Provides clarifications or summaries for study materials.

### **3. Interactive Chat Interface**

* Seamlessly interact with DocuMind in a **chat-like interface**.
* History of your questions and AI responses maintained for session continuity.

### **4. Context Management**

* Process multiple documents and images at once.
* Clear content context with a single click to start fresh.

### **5. Easy Deployment**

* Lightweight **Streamlit** app that runs locally or can be deployed to the cloud.
* Fully environment-variable configured (`.env`) for secure API management.

---

## 🎯 Supported File Types

| Type          | Description                             |
| ------------- | --------------------------------------- |
| PDF           | `.pdf` files, text extracted from pages |
| Word Document | `.docx` files                           |
| Plain Text    | `.txt` files                            |
| Images        | `.png`, `.jpg`, `.jpeg`                 |

---

## 💻 Getting Started

### **1. Clone the Repository**

```bash
git clone https://github.com/surajksharma7/documind.git
cd documind
```

### **2. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **3. Configure OpenAI API Key**

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_openai_api_key_here
```

### **4. Run the App**

```bash
streamlit run app.py
```

Open the browser at `http://localhost:8501` and start interacting with DocuMind.

---

## 🛠️ Code Overview

**Main Features & Files:**

* `app.py` – Streamlit frontend and chat interface.
* `utils/` – Helper functions for file reading and content extraction.
* `ChatOpenAI` – Connects with OpenAI’s GPT-4o for multimodal understanding.
* `session_state` – Maintains chat history, text context, and image context.

**Key Functions:**

```python
def extract_text_from_pdf(file) -> str
def extract_text_from_docx(file) -> str
def extract_text_from_txt(file) -> str
```

These functions read content from various file types to feed into the AI.

**Chat Flow:**

1. User uploads content (text or image) or pastes text.
2. DocuMind stores content in `st.session_state`.
3. User asks a question.
4. AI constructs a dynamic prompt with context.
5. Response displayed in the interactive chat interface.

---

## 📷 Example Screenshots

**Upload Sidebar & Text Input**
![Sidebar](https://placehold.co/600x400?text=Sidebar+with+upload+options)

**Chat Interaction**
![Chat](https://placehold.co/600x400?text=Chat+interface+with+AI+response)

---

## 💡 Use Cases

* Students studying multiple subjects.
* Researchers summarizing papers.
* Professionals analyzing reports.
* Anyone looking to convert documents and images into interactive learning material.

---

## ⚡ Future Enhancements

* **Automatic summarization** of large PDFs.
* **Keyword extraction** and **flashcard generation**.
* **Advanced image analysis** (charts, diagrams, handwritten notes).
* **Multi-language support**.

---

## 📄 License

MIT License © [Suraj Kumar Sharma](https://github.com/surajksharma7)

---

## 📞 Contact

For support, feedback, or contributions:
**Email:** [surajksharma2304@gmail.com](mailto:surajksharma2304@gmail.com)
**GitHub:** [github.com/surajksharma7](https://github.com/surajksharma7)