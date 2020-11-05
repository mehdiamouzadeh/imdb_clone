from django.urls import path
from movie.views import index,paginate

urlpatterns = [
    path('',index,name='index'),
    path('search/<query>/page/<page_number>',paginate,name='paginate')
]
