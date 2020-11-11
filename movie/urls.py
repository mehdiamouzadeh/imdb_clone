from django.urls import path
from movie.views import index,paginate,movieDetails,genres

urlpatterns = [
    path('',index,name='index'),
    path('search/<query>/page/<page_number>',paginate,name='paginate'),
    path('<imdb_id>', movieDetails, name='movie-details'),
    path('genre/<slug:genre_slug>',genres,name="genres"),
]
