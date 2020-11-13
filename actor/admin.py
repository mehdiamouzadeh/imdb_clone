from django.contrib import admin
from movie.models import Movie,Genre
from actor.models import Actor
# Register your models here.

admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Genre)