from django.contrib import admin
# from .models import Attribute, Location, Trainer, Charmander, Bulbasaur, Squirtle, Pokemon
from .models import Charmander, Squirtle, Bulbasaur, Trainer, Location
# Register your models here.
admin.site.register(Location)
admin.site.register(Trainer)
admin.site.register(Charmander)
admin.site.register(Bulbasaur)
admin.site.register(Squirtle)
# admin.site.register(Attribute)
# admin.site.register(Pokemon)
