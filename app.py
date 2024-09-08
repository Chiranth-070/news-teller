import os
import streamlit as st
from dotenv import load_dotenv
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain.docstore.document import Document
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import WebBaseLoader

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANG_CHAIN")
os.environ["NVIDIA_API_KEY"] = os.getenv("NVIDIA_API_KEY")


def geturl_text(article_url):
    loader = WebBaseLoader(article_url)

    docs = loader.load()
    content = ""
    for i in range(len(docs)):
        content += docs[i].page_content
    
    return content


def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=40, length_function=len, )
    document = Document(page_content=text)
    splits = text_splitter.split_documents([document])
    text_chunks = [split.page_content for split in splits]
    return text_chunks


def get_vector_store(text_chunks):
    embedder = NVIDIAEmbeddings(model="NV-Embed-QA")
    vector_store = FAISS.from_texts(text_chunks, embedding=embedder)
    vector_store.save_local("faiss_index")


def get_conversational_chain():
    prompt_template = """
        Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
        provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
        Context:\n {context}?\n
        Question: \n{question}\n

        Answer:
        """
    model = ChatNVIDIA(model="meta/llama3-70b-instruct")

    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain


def user_input(user_question):
    embedder = NVIDIAEmbeddings(model="NV-Embed-QA")
    new_db = FAISS.load_local("faiss_index", embedder, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question, k=5)

    chain = get_conversational_chain()
    response = chain(
        {"input_documents": docs, "question": user_question},
        return_only_outputs=True
    )
    st.write("Reply: ", response["output_text"])


def main():
    st.header("News Article Q&A 📰")

    user_question = st.text_input("Ask a Question from the Article")

    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Enter the URL")
        st.write("Enter the URL of the news article you want to ask questions about")
        article_url = st.text_input("URL")
        if st.button("Get Article"):
            with st.spinner("Getting article..."):
                content = geturl_text(article_url)
                text_chunks = get_text_chunks(content)
                get_vector_store(text_chunks)
                if text_chunks:
                    st.success("article processed")
                else:
                    st.error("unable to process article")

if __name__ == "__main__":
    main()