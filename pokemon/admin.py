from django.contrib import admin
# from .models import Attribute, Capture, Trainer, Charmander, Bulbasaur, Squirtle, Pokemon
from .models import Pokemon, PokemonCategory, Trainer, Capture
# Register your models here.
admin.site.register(Capture)
admin.site.register(Trainer)
# admin.site.register(Attribute)
admin.site.register(Pokemon)

