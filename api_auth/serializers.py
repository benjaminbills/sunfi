# Django rest framework imports
from rest_framework import serializers

# Import User from api_auth
from .models import User

# Create serializer for User Model


class UserSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField(read_only=True)
    id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ["id", "user_name", "email"]

    def get_id(self, obj):
        return obj.id

    def get_user_name(self, obj):
        user_name = obj.user_name
        if user_name == "":
            user_name = obj.email
        return user_name
