import os

from langchain.document_loaders import UnstructuredPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List
from config import OPENAI_API


def load_pdf_doc(path_to_doc: str) -> List:
    """ """
    loader = UnstructuredPDFLoader(path_to_doc)
    data_from_pdf = loader.load()

    return data_from_pdf


def split_loaded_pdf_data(data_from_pdf: List) -> List:
    """ """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=4000,
        chunk_overlap=200,
        length_function=len,
        add_start_index=True,
    )

    splitted_data_from_pdf = text_splitter.create_documents([data_from_pdf[0].page_content])

    return splitted_data_from_pdf





