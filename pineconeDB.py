from langchain import PromptTemplate, ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.memory import VectorStoreRetrieverMemory
from langchain.retrievers import PineconeHybridSearchRetriever
from langchain.vectorstores import Pinecone
import os
import pinecone
from typing import List

from pinecone_text.sparse import bm25_encoder

from config import PINECONE_ENV, PINECONE_API_KEY, INDEX_NAME, OPENAI_API

os.environ['OPENAI_API_KEY'] = OPENAI_API

pinecone.init(
    api_key=PINECONE_API_KEY,
    environment=PINECONE_ENV
)
embeddings = OpenAIEmbeddings()
index = pinecone.Index(INDEX_NAME)

vectorstore = Pinecone(index, embeddings.embed_query, 'text')

retriever = vectorstore.as_retriever(search_kwargs=dict(k=1))
memory = VectorStoreRetrieverMemory(retriever=retriever)

print('memory was loaded')




def search_in_pinecone_without_context(query):
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")  # Can be any valid LLM
    _DEFAULT_TEMPLATE = """
        {history}
    
        {input}
    """
    PROMPT = PromptTemplate(
        input_variables=["history", "input"], template=_DEFAULT_TEMPLATE
    )
    conversation_with_summary = ConversationChain(
        llm=llm,
        prompt=PROMPT,

        memory=memory,
        verbose=False
    )
    inp = f"""{query}"""

    output = conversation_with_summary.predict(input=inp)

    return output

    def search_in_pinecone_with_context():
        pass
        # memory.save_context({"input": input}, {"output": output})


if __name__ == '__main__':

    pass
