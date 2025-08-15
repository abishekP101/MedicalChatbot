from dotenv import load_dotenv
import os
load_dotenv()
from src.helper import (
    load_pdf_files,
    filter,
    split_documents,
    download_hugingface_model
)
from pinecone import Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

extracted_docs = load_pdf_files("data/")
filtered_docs = filter(extracted_docs)
split_docs = split_documents(filtered_docs)

embedding = download_hugingface_model()

pinecone_api_key = PINECONE_API_KEY
pc = Pinecone(api_key=pinecone_api_key)

index_name = "medical-chatbot"

if not pc.has_index(index_name):
    pc.create_index(
        index_name,
        dimension=384,  # Dimension of the embeddings
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region='us-east-1'
        ),
    )

index = pc.Index(index_name)

docsearch = PineconeVectorStore.from_documents(
    documents=split_docs,
    embedding=embedding,
    index_name=index_name,
    namespace="medical-chatbot"
)