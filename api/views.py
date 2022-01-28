from django.shortcuts import render
from rest_framework.decorators import api_view
import requests
from rest_framework.response import Response
from decouple import config

# Create your views here.
Authorization = config('AUTHORIZATION')
@api_view(['GET'])
def list(request):
  r = requests.get('https://the-one-api.dev/v2/character', headers={'Authorization': Authorization})
  print(r)
  return Response('working')
