from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

loader = PyPDFLoader(r"document loader\RAG system.pdf")
documents = loader.load()

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

model = ChatMistralAI(model="mistral-small-2603")

prompt = template.format_messages(
    document=documents[0].page_content
)

result = model.invoke(prompt)

print(result.content)


# Context Window:
# In a RAG system, the retrieved document chunks are sent to the LLM as context.
# Since every LLM has a limited context window, only the most relevant chunks
# can be included in a single request to ensure accurate and efficient responses