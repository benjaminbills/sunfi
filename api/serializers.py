from rest_framework import serializers
from .models import Character, FavoriteCharacter, FavoriteQuote, Quote
from api_auth.serializers import UserSerializer
from api_auth.models import User
class CharacterSerializer(serializers.ModelSerializer):
  class Meta:
    model = Character
    fields = '__all__'

class QuoteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Quote
    fields = '__all__'

class FavoriteCharacterSerializer(serializers.ModelSerializer):
  user = serializers.SerializerMethodField(read_only=True)
  character = serializers.SerializerMethodField(read_only=True)
  class Meta:
    model = FavoriteCharacter
    fields = '__all__'
  def get_user(self, obj):
    user = obj.user
    serailizer = UserSerializer(user, many=False)
    return serailizer.data
  def get_character(self, obj):
    character = obj.character
    serailizer = CharacterSerializer(character, many=False)
    return serailizer.data



class FavoriteQuoteSerializer(serializers.ModelSerializer):
  quote = serializers.SerializerMethodField(read_only=True)
  user = serializers.SerializerMethodField(read_only=True)
  class Meta:
    model = FavoriteQuote
    fields = ('quote', 'user')
  def get_user(self, obj):
    user = obj.user
    serailizer = UserSerializer(user, many=False)
    return serailizer.data
  def get_quote(self, obj):
    quote = obj.quote
    serailizer = QuoteSerializer(quote, many=False)
    return serailizer.data

