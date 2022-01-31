from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, UserSerializer


# Create your views here.


from .models import User

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
  def validate(self, attrs):
      data = super().validate(attrs)

      serializer = UserSerializer(self.user).data

      for k, v in serializer.items():
        data[k] = v
      # data.pop('refresh',None)
      return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


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
