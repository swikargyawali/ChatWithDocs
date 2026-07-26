from langchain_community.document_loaders import WebBaseLoader

url= "https://www.apple.com/"

loader=WebBaseLoader(url)

documents=loader.load()

print(len(documents[0].page_content))