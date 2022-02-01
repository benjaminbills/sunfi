from rest_framework import serializers
from .models import Character, FavoriteCharacter, FavoriteQuote, Quote
from api_auth.serializers import UserSerializer
from api_auth.models import User


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = "__all__"


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = "__all__"


class FavoriteCharacterSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField(read_only=True)
    character = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = FavoriteCharacter
        fields = ["character"]

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
    # user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = FavoriteQuote
        fields = ["quote"]

    def get_user(self, obj):
        user = obj.user
        serailizer = UserSerializer(user, many=False)
        return serailizer.data

    def get_quote(self, obj):
        quote = obj.quote
        serailizer = QuoteSerializer(quote, many=False)
        return serailizer.data


class AllFavorite(serializers.ModelSerializer):
    id = serializers.SerializerMethodField(read_only=True)
    quotes = serializers.SerializerMethodField(read_only=True)
    character = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ["id", "user_name", "email", "quotes", "character"]

    def get_id(self, obj):
        return obj.id

    def get_quotes(self, obj):
        quotes = FavoriteQuote.objects.filter(user=obj.id)
        serializer = FavoriteQuoteSerializer(quotes, many=True)
        return serializer.data

    def get_character(self, obj):
        quotes = FavoriteCharacter.objects.filter(user=obj.id)
        serializer = FavoriteCharacterSerializer(quotes, many=True)
        return serializer.data
