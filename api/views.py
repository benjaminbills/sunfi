# Request import
import requests

# Django rest framework imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

# Import from apps
from api_auth.models import User
from core.settings import ONE_AUTH
from api.serializers import AllFavorite, FavoriteCharacterSerializer, FavoriteQuoteSerializer
from .models import Character, FavoriteCharacter, FavoriteQuote, Quote

# Views and functions.
# Get Characters from API

# Declare request url.
url = 'https://the-one-api.dev/v2/'

# Get characters
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_characters(request):
  r = requests.get(f'{url}character', headers={'Authorization': ONE_AUTH})
  characters = r.json()['docs']
  return Response(characters)

# Get character and quotes
@api_view(['GET'])
def get_charater_quotes(request, pk):
  r = requests.get(f'{url}character/{pk}/quote', headers={'Authorization': ONE_AUTH}).json()
  data = r['docs']
  if len(data) == 0:
    return Response({f'No quote from charater with id {pk}'})
  return Response(data)

# Add favorite character
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_favorite(request, pk):
    user = request.user
    character = check_or_get_character(pk)
    if hasattr(character, 'status_code'):
      return character
    else:
      favorite = FavoriteCharacter.objects.get_or_create(user=user, character=character)
      serializer = FavoriteCharacterSerializer(favorite[0], many=False)
      return Response(serializer.data)

# Add favorite quote
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_favorite_quote(request, pk_c, pk_q):
    user = request.user
    print(user)
    character = check_or_get_character(pk_c)
    if hasattr(character, 'status_code'):
      return character
    else:
      r = requests.get(f'{url}quote/{pk_q}', headers={'Authorization': ONE_AUTH})
      if r.status_code == 500:
        return Response({'message':f'quote with id:{pk_q} does not exist'})
      else:
        data = r.json()['docs'][0]
        quote = Quote.objects.get_or_create(
          id = data['_id'], dialog = data['dialog'], movie_id = data['movie'], character = character
        )
        favorite_quote = FavoriteQuote.objects.get_or_create(user=user, quote=quote[0])
        
        serializer = FavoriteQuoteSerializer(favorite_quote[0], many=False)
        return Response(serializer.data)

# Get all users favorite quotes and character
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_favorites(request):
  users = User.objects.all()
  serializer = AllFavorite(users, many=True)
  return Response(serializer.data)


# Get character from one api and store to DB
def check_or_get_character(pk_c):
  character = {}
  try:
    character = Character.objects.get(id=pk_c)
  except:
    r_character = requests.get(f'{url}character/{pk_c}/', headers={'Authorization': ONE_AUTH})
    if r_character.status_code == 500:
      return  Response({'message':f'Character with the id:{pk_c} does not exist'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    if int(r_character.json()['total']) == 0:
      return  Response({'message':f'Character with the id:{pk_c} does not exist'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    else :
      print(r_character)
      data = r_character.json()['docs'][0]
      character = Character.objects.create(
        id = data['_id'], height=data['height'], race=data['race'].strip('"'), birth=data['birth'].strip('"'),death=data['death'].strip('"'),realm=data['realm'].strip('"'),hair=data['hair'].strip('"'),name=data['name'],wikiUrl= data['wikiUrl']
      )
  return character

