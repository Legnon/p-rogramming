from django.db import models

class Location(models.Model):
    lnglat = models.CharField(max_length=20)
    def __str__(cls):
        return cls.lnglat

class Trainer(models.Model):
    name = models.CharField(max_length=20)
    def __str__(cls):
        return cls.name

class Pokemon(models.Model):
    description = '포켓몬'
    attribute = {
        'Fire': '불',
        'Water': '물',
        'Leaf': '풀',
    }

class Charmander(Pokemon):
    category = '파이리'
    attribute = (Pokemon.attribute['Fire'])
    url = 'http://pokedex.pokemonkorea.co.kr/templates/default/images/MonImages/middle/005_004.png'
    name = models.CharField(max_length=20, default=category)
    location = models.ForeignKey(Location, null=True)
    trainer = models.ForeignKey(Trainer, null=True)
    def __str__(cls):
        return cls.name

class Squirtle(Pokemon):
    category = '꼬부기'
    attribute = (Pokemon.attribute['Water'])
    url = 'http://pokedex.pokemonkorea.co.kr/templates/default/images/MonImages/middle/010_007.png'
    name = models.CharField(max_length=20, default=category)
    location = models.ForeignKey(Location, null=True)
    trainer = models.ForeignKey(Trainer, null=True)
    def __str__(cls):
        return cls.name

class Bulbasaur(Pokemon):
    category = '이상해씨'
    attribute = (Pokemon.attribute['Leaf'])
    url = 'http://pokedex.pokemonkorea.co.kr/templates/default/images/MonImages/middle/001_001.png'
    name = models.CharField(max_length=20, default=category)
    location = models.ForeignKey(Location, null=True)
    trainer = models.ForeignKey(Trainer, null=True)
    def __str__(cls):
        return cls.name

