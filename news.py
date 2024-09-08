from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://timesofindia.indiatimes.com/city/patna/9-year-old-boy-beheaded-in-bihars-begusarai/articleshow/113161452.cms")

docs = loader.load()

length_of_docs = len(docs)

for i in range(length_of_docs):
    print(docs[i].page_content)