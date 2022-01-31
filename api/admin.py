from django.contrib import admin

from api.models import Character, FavoriteCharacter, FavoriteQuote, Quote

# Register your models here.
admin.site.register(Character)
admin.site.register(FavoriteCharacter)
admin.site.register(Quote)
admin.site.register(FavoriteQuote)
