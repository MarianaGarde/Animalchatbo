from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from pinecone import Pinecone
from langchain_community.vectorstores import Pinecone as PC
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')

#pdf loading
extracted_data=load_pdf("data/")
#chunks of text
text_chunks=text_split(extracted_data)
print(len(text_chunks))
#embeddings
embeddings=download_hugging_face_embeddings()

#init Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index("animalchatbot")
index_name='animalchatbot'
#data storing

docsearch =PC.from_texts([t.page_content for t in text_chunks], embeddings, index_name=index_name)