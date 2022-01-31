from django.urls import path
from .views import registerUser, MyTokenObtainPairView, MyTokenObtainPairSerializer

urlpatterns = [
    # path('', views.getUsers, name='getUsers'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', registerUser, name='registerUser'),
]
