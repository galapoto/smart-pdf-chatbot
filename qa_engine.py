from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.openai import OpenAI
from utils import OPENAI_API_KEY

llm = OpenAI(api_key=OPENAI_API_KEY, model="gpt-3.5-turbo", temperature=0)

def build_index_from_text(text):
    with open("temp.txt", "w", encoding="utf-8") as f:
        f.write(text)

    documents = SimpleDirectoryReader(input_files=["temp.txt"]).load_data()
    index = VectorStoreIndex.from_documents(documents, llm=llm)
    return index

def ask_question(index, query):
    engine = index.as_query_engine()
    return engine.query(query)