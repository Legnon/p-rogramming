from django.shortcuts import render
from .models import Charmander, Squirtle, Bulbasaur
from django.views.generic.list import ListView
import os
import json

def poke_list(request):
    charmander = Charmander.objects.all()
    squirtle = Squirtle.objects.all()
    bulbasaur = Bulbasaur.objects.all()
    if charmander.count() == 0:
        charmander = Charmander()
    if squirtle.count() == 0:
        squirtle = Squirtle()
    if bulbasaur.count() == 0:
        bulbasaur = Bulbasaur()
    pokemon = {
        'charmander': charmander,
        'squirtle': squirtle,
        'bulbasaur': bulbasaur,
    }
    return render(request, 'pokemon/pokemon_list.html', pokemon)

# json parsing
def poke_json(request):
    file_path = os.path.join(os.path.dirname(__file__), '../programming/static/pokemon.json')
    obj = open(file_path).read()
    obj_json = json.loads(obj)
    return render(request, 'pokemon/pokemon_json.html', {'pokemon': obj_json})

