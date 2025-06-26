# 🤖 Smart PDF Chatbot

A Streamlit-powered AI chatbot that allows users to ask questions about the content of PDF documents using OpenAI and LlamaIndex.

## 🔍 Features

- 📄 Upload PDF and automatically extract the content
- 💬 Ask questions based on document content
- 🧠 Powered by LlamaIndex and OpenAI LLMs
- 🖥️ Clean UI built with Streamlit
- 🔐 Environment-based API key loading for security

## 🚀 How It Works

1. Upload your PDF file.
2. The file is parsed into raw text.
3. A vector index is built using LlamaIndex.
4. Ask questions and receive context-aware answers from OpenAI GPT.

---

## 📦 Dependencies

- `streamlit`
- `llama-index`
- `PyMuPDF` (for PDF parsing)
- `python-dotenv`
- `openai`

Install all dependencies:

```bash
pip install -r requirements.txt

🛠️ Setup
Clone the Repository
git clone https://github.com/your-username/smart-pdf-chatbot.git
cd smart-pdf-chatbot

Set Your OpenAI API Key
Create a .env file at the root:
echo "OPENAI_API_KEY=your_openai_key_here" > .env
Or use secrets.toml for Streamlit Cloud:
# .streamlit/secrets.toml
OPENAI_API_KEY = "your_openai_key_here"

Run the App
streamlit run app.py

Example Use Case
Upload a Finnish government housing PDF, then ask:
"Who is eligible for general housing allowance?"
The app will return answers sourced directly from the document.

📁 Folder Structure
smart-pdf-chatbot/
├── app.py
├── qa_engine.py
├── utils.py
├── .env (or .streamlit/secrets.toml)
├── requirements.txt
├── README.md

🔒 Security
❗ Never commit your OpenAI API key!
Always use environment variables or secrets.toml.

📤 Deployment (Streamlit Cloud)
Push to GitHub (see instructions below).
Go to https://share.streamlit.io and connect your repo.
Add your OpenAI key in App Settings → Secrets.

📘 License
MIT License © 2025 Vitus Idi