from langchain_community.document_loaders import PyPDFLoader , DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Pinecone
from langchain.embeddings import HuggingFaceEmbeddings

def load_pdf_files(directory):
    loader=DirectoryLoader(directory, glob="**/*.pdf" , loader_cls=PyPDFLoader)

    documents = loader.load()
    return documents


from typing import List
from langchain.schema import Document
def filter(docs: List[Document]) -> List[Document]:
    """
    Load all PDF files from a specified directory.
    """
    minimal_docs: List[Document] = []
    for doc in docs:
        src = doc.metadata.get("source")
        minimal_docs.append(
            Document(
                page_content=doc.page_content,
                metadata={
                    "source": src}
            )
        )
    return minimal_docs


def split_documents(documents):
    """
    Split documents into smaller chunks.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=30,
    )
    
    return text_splitter.split_documents(documents)


def download_hugingface_model():
    """
    Download a model from Hugging Face.
    """
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embedding = HuggingFaceEmbeddings(model_name=model_name)

    return embedding

