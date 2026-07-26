from langchain_community.document_loaders import PyPDFLoader

data= PyPDFLoader("RAG system.pdf")

documents=data.load()

print(documents[17])