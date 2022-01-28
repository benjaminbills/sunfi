from django.contrib import admin

from api.models import Character, Favorite

# Register your models here.
admin.site.register(Character)
admin.site.register(Favorite)