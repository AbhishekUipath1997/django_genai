import json
import os
import random
import sys
import requests
from django.http import JsonResponse

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from google.protobuf.json_format import MessageToDict
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

# For GenAI 


#from flask import Flask, jsonify, request
#from flask_cors import CORS, cross_origin

#import json
#import os
#import sys
#import boto3


#from langchain_community.embeddings import BedrockEmbeddings
#from langchain.llms.bedrock import Bedrock




#import numpy as np
#from langchain.text_splitter import RecursiveCharacterTextSplitter
#from langchain_community.document_loaders import PyPDFDirectoryLoader



#from langchain.vectorstores import FAISS


#from langchain.prompts import PromptTemplate
#from langchain.chains import RetrievalQA


class GenAIWebhook(generics.GenericAPIView):
    permission_classes = []

    def __init__(self, **kwargs):
        print("inside GenAIWebhook:  hello from GENAI")
        super().__init__(**kwargs)
        self.request_data = None
        self.agent_request_body=None
        self.received_msg = None
        self.conversation_id = None
        self.user = None
        self.bot_id = None
        self.web_uid = None
        self.platform = None
        self.nlp_agent = None
        self.agentId = None

    
   
    def post(self, request, *arg, **kwargs):
        data={"response":"API is working!!"}
        return JsonResponse(status=status.HTTP_200_OK, data=data)

    @csrf_exempt
    @renderer_classes(JSONRenderer)
    def GenAI_response(self, request, *arg, **kwargs):
       try:
           print("inside try block!!")
           print("Request data",self.body)
           data = self.body
           return JsonResponse(status=status.HTTP_200_OK, data=data)
       except Exception as e:
           print("process message exception", e)


