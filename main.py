from dotenv import load_dotenv 
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

loader=TextLoader("notes.txt")
documents=loader.load()

template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are an expert AI assistant that summarizes documents.

Your task is to generate a clear, concise, and accurate summary of the provided document.
Focus on the main ideas, important concepts, and key takeaways while preserving the original meaning.
Do not add information that is not present in the document.
"""
        ),
        (
            "human",
            """Please summarize the following document:

{document}
"""
        )
    ]
)

model= ChatMistralAI (model="mistral-small-2603")

prompt=template.format_messages(loader= documents[0].page_content)

result= model.invoke("Helloo")
print(result.content)