# Core Django Imports
from django.contrib.auth.hashers import make_password

# Django rest framework imports
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Import from project apps
from .serializers import UserSerializer
from .models import User

# Views

# Obtain token
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
  def validate(self, attrs):
      data = super().validate(attrs)

      serializer = UserSerializer(self.user).data

      for k, v in serializer.items():
        data[k] = v
      data.pop('refresh',None)
      return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# Register user
@api_view(['POST'])
def registerUser(request):
  data=request.data
  try:
    user = User.objects.create(
      user_name = data['username'],
      email = data['email'],
      password = make_password(data['password'])
    )
    serializer = UserSerializer(user, many=False)
    
    return Response(serializer.data)
  except:
    message = {'detail':'User with this email or username already exist'}
    return Response(message, status=status.HTTP_400_BAD_REQUEST)
