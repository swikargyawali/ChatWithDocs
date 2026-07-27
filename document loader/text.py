from langchain_community.document_loaders import TextLoader

from langchain_text_splitters import CharacterTextSplitter

splitter=CharacterTextSplitter(
    separator="\n\n",
    chunk_size=1000,
    chunk_overlap=200,
)

loader=TextLoader("notes.txt")
documents=loader.load()


chunks=splitter.split_documents(documents)


# The `load()` method returns a list of Document objects.
#
# Why a list?
# A document loader may load one or multiple documents depending on the source.
# For example:
# - A TextLoader loads a single text file.
# - A DirectoryLoader can load multiple files from a folder.
# - A PDF loader may return one Document per page or the entire PDF, depending on the loader.
#
# Each Document object contains:
# - page_content : The actual text extracted from the document.
# - metadata     : Additional information about the document, such as the
#                  source file, page number, title, etc.
#
# Since `load()` always returns a list, we access the first document using:
# documents[0]

for i in chunks:
    print(i.page_content)
    print()
    print()
    print()

