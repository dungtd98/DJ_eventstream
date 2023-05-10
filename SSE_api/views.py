from django.shortcuts import render
from rest_framework.views import APIView
from django_eventstream.eventstream import send_event
from rest_framework.response import Response
from rest_framework import status
import openai
import os
from dotenv import load_dotenv
load_dotenv(".env")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
# Create your views here.
openai.api_key = OPENAI_API_KEY
def ask_open_ai(prompt, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model = model,
        messages=[
                {"role": "user", "content": prompt}
            ],
        temperature = 0.5,
        stream=True  
    )
    answer = ''
    for chunk in response:
        answer+=chunk['choices'][0]['delta'].get('content','')
        send_event('test','message',answer)
class QuestionApiView(APIView):
    def post(self, request, *args, **kwargs):
        ask_open_ai(request.data['prompt'])
        return Response({'detail':"Ok"}, status=status.HTTP_200_OK)