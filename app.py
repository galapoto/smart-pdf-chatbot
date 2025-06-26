import streamlit as st
from utils import extract_text_from_pdf
from qa_engine import build_index_from_text, ask_question

st.set_page_config(page_title="PDF Q&A Bot")
st.title("📄 Ask Questions About Your PDF")

uploaded = st.file_uploader("Upload a PDF", type="pdf")
if uploaded:
    with open("uploaded.pdf", "wb") as f:
        f.write(uploaded.read())
    st.success("PDF uploaded!")

    if st.button("Build Q&A Index"):
        with st.spinner("Processing PDF..."):
            raw_text = extract_text_from_pdf("uploaded.pdf")
            index = build_index_from_text(raw_text)
            st.session_state.index = index
        st.success("Ready! Ask your question below.")

if "index" in st.session_state:
    question = st.text_input("Your question:")
    if question:
        answer = ask_question(st.session_state.index, question)
        st.markdown(f"**Answer:** {answer.response}")