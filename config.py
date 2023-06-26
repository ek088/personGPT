import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API = os.environ['OPENAI_API']
PINECONE_API_KEY = os.environ['PINECONE_API_KEY']
PINECONE_ENV = os.environ['PINECONE_ENV']
