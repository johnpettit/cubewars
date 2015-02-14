from django.contrib import admin
from mycubewars.models import Account, Character, Profession, Game
# Register your models here.

admin.site.register(Account)
admin.site.register(Character)
admin.site.register(Profession)
admin.site.register(Game)
