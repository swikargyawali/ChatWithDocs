from langchain_community.document_loaders import PyPDFLoader

data= PyPDFLoader("GRU.pdf")

documents=data.load()

