from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from pinecone import Pinecone
from langchain_community.vectorstores import Pinecone as PC
from langchain import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.llms import CTransformers
from dotenv import load_dotenv
from src.prompt import *
import os


app= Flask(__name__)