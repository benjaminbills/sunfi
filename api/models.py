from django.db import models

# Create your models here.
class Character(models.Model):
  id = models.CharField(primary_key=True, max_length=100)
  height = models.CharField(max_length=5, blank=True, null=True)
  race = models.CharField(max_length=100)
  birth = models.CharField(max_length=100)
  death = models.CharField(max_length=100)
  realm = models.CharField(max_length=100)
  hair = models.CharField(max_length=100)
  name =models.CharField(max_length=100)
  wikiUrl = models.URLField(max_length=100)

class Favorite (models.Model):
  character = models.ForeignKey(Character, on_delete=models.CASCADE)
