from rest_framework import serializers, status
from django.shortcuts import render
from rest_framework.decorators import api_view
import requests
from rest_framework.response import Response
from decouple import config
from core.settings import ONE_AUTH
from .models import Character, FavoriteCharacter, Quote
# Create your views here.

@api_view(['GET'])
def get_characters(request):
  r = requests.get('https://the-one-api.dev/v2/character', headers={'Authorization': ONE_AUTH}).json()
  characters = r['docs']
  return Response(characters)

@api_view(['GET'])
def get_charater_quotes(request, pk):
  r = requests.get(f'https://the-one-api.dev/v2/character/{pk}/', headers={'Authorization': ONE_AUTH}).json()
  data = r['docs']
  name = data[0]['race']
  print(len(data))
  return Response(name)

@api_view(['POST'])
def add_favorite(request, pk):
    character = check_or_get_character(pk)
    print(character)
    if hasattr(character, 'status_code'):
      return character
    else:
      favorite = FavoriteCharacter.objects.create(character=character)
      return Response('workinh here')


@api_view(['POST'])
def add_favorite_quote(request, pk_c, pk_q):
    character = check_or_get_character(pk_c)
    if hasattr(character, 'status_code'):
      return character
    else:
      r = requests.get(f'https://the-one-api.dev/v2/quote/{pk_q}', headers={'Authorization': ONE_AUTH})
      if r.status_code == 500:
        return Response({'message':f'quote with id:{pk_q} does not exist'})
      else:
        data = r.json()['docs'][0]
        quote = Quote.objects.create(
          id = data['_id'], dialog = data['dialog'], movie_id = data['movie'], character = character
        )
        return Response(data)


def check_or_get_character(pk_c):
  character = {}
  try:
    character = Character.objects.get(id=pk_c)
  except:
    r_character = requests.get(f'https://the-one-api.dev/v2/character/{pk_c}/', headers={'Authorization': ONE_AUTH})
    if r_character.status_code == 500:
      return  Response({'message':f'Character with the id:{pk_c} does not exist'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    else :
      data = r_character.json()['docs'][0]
      character = Character.objects.create(
        id = data['_id'], height=data['height'], race=data['race'].strip('"'), birth=data['birth'].strip('"'),death=data['death'].strip('"'),realm=data['realm'].strip('"'),hair=data['hair'].strip('"'),name=data['name'],wikiUrl= data['wikiUrl']
      )
  return character

