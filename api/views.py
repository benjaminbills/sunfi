import re
from tabnanny import check
from django.shortcuts import render
from rest_framework.decorators import api_view
import requests
from rest_framework.response import Response
from decouple import config
from core.settings import ONE_AUTH
from .models import Character, Favorite
# Create your views here.

@api_view(['GET'])
def get_characters(request):
  r = requests.get('https://the-one-api.dev/v2/character', headers={'Authorization': ONE_AUTH}).json()
  data = r['docs']
  print(len(data))
  return Response(data)

@api_view(['GET'])
def get_charater_quotes(request, pk):
  r = requests.get(f'https://the-one-api.dev/v2/character/{pk}/', headers={'Authorization': ONE_AUTH}).json()
  data = r['docs']
  name = data[0]['race']
  print(len(data))
  return Response(name)

@api_view(['POST'])
def add_favorite(request, pk):
  try:
    check_character = Character.objects.get(id=pk)
    check_favorite = Favorite.objects.get(character=check_character)
    print(check_favorite==None)
    # favorite = Favorite.objects.create(character=check_character)
  except:
    r = requests.get(f'https://the-one-api.dev/v2/character/{pk}/', headers={'Authorization': ONE_AUTH}).json()
    if r['success'] == False:
      print('no data')
    else:
      # print('No data')
      data = r['docs'][0]
      character = Character.objects.create(
        id = data['_id'], height=data['height'], race=data['race'].strip('"'), birth=data['birth'].strip('"'),death=data['death'].strip('"'),realm=data['realm'].strip('"'),hair=data['hair'].strip('"'),name=data['name'],wikiUrl= data['wikiUrl']
      )
      favorite = Favorite.objects.create(character=character)
      print(character)
  # # favorite.
  return Response('working')


