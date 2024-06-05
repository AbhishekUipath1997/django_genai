import json
import os
import random
import sys

import boto3
from langchain_community.embeddings import BedrockEmbeddings
from langchain.llms.bedrock import Bedrock
import numpy as np
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA


from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from google.protobuf.json_format import MessageToDict




prompt_template = """

Human: Use the following pieces of context to provide a 
concise answer to the question at the end but usse atleast summarize with 
250 words with detailed explaantions. If you don't know the answer, 
just say that you don't know, don't try to make up an answer.
<context>
{context}
</context

Question: {question}

Assistant:"""

PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)



bedrock=boto3.client(service_name="bedrock-runtime", region_name='us-east-1')
bedrock_embeddings=BedrockEmbeddings(model_id="amazon.titan-embed-text-v1",client=bedrock)


def data_ingestion():
    try:
        print("inside--->data_ingestion")
        loader=PyPDFDirectoryLoader("/opt/GenAI_Doc/genai_doc/data")
        print("data_ingestion_loader",loader)
        documents=loader.load()
        print("documentsdocuments",documents)
        text_splitter=RecursiveCharacterTextSplitter(chunk_size=10000,chunk_overlap=1000)
        print("text_splitter-->",text_splitter)
        docs=text_splitter.split_documents(documents)
        print("len()",len(docs))
        return docs
    except Exception as e:
        return e

def get_vector_store(docs):
    vectorstore_faiss=FAISS.from_documents(docs,bedrock_embeddings)
    vectorstore_faiss.save_local("/opt/GenAI_Doc/genai_doc/faiss_index/faiss_index")

def get_claude_llm():
    llm=Bedrock(model_id="ai21.j2-mid-v1",client=bedrock,model_kwargs={'maxTokens':512})
    return llm


def get_llama2_llm():
    llm=Bedrock(model_id="meta.llama2-70b-chat-v1",model_kwargs={'max_gen_len':512})
    return llm

def get_response_llm(llm,vectorstore_faiss,query):
    qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore_faiss.as_retriever(
        search_type="similarity", search_kwargs={"k": 3}
    ),
    return_source_documents=True,
    chain_type_kwargs={"prompt": PROMPT}
    )
    answer=qa({"query":query})
    return answer['result']
