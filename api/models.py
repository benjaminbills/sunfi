from django.db import models
from api_auth.models import User
# Create your models here.
class Character(models.Model):
  id = models.CharField(primary_key=True, unique=True, max_length=100)
  height = models.CharField(max_length=5, blank=True, null=True)
  race = models.CharField(max_length=100)
  birth = models.CharField(max_length=100)
  death = models.CharField(max_length=100)
  realm = models.CharField(max_length=100)
  hair = models.CharField(max_length=100)
  name =models.CharField(max_length=100)
  wikiUrl = models.URLField(max_length=100)

class FavoriteCharacter(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  character = models.ForeignKey(Character, on_delete=models.CASCADE)

class Quote (models.Model):
  id = models.CharField(primary_key=True,unique=True, max_length=100)
  dialog=models.CharField(max_length=500)
  movie_id = models.CharField(max_length=50)
  character = models.ForeignKey(Character, on_delete=models.CASCADE)

class FavoriteQuote(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  quote = models.ForeignKey(Quote, on_delete=models.CASCADE)