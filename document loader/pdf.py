from langchain_community.document_loaders import PyPDFLoader

loader= PyPDFLoader("RAG system.pdf")

documents=loader.load()

print(documents[17])