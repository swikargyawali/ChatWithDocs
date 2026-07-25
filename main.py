from dotenv import load_dotenv 
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

loader=TextLoader("notes.txt")
documents=loader.load()

template=ChatPromptTemplate.from_messages(
    [("system","you are an AI that summarize this text"),
     ("human","{loader}")]
)

model= ChatMistralAI (model="mistral-small-2603")

prompt=template.format_messages(loader= documents[0].page_content)

result= model.invoke("Helloo")
print(result.content)