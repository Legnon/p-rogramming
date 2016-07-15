from django.shortcuts import render
from .models import Charmander, Squirtle, Bulbasaur
from django.views.generic.list import ListView


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
