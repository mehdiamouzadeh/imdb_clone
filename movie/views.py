from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.template import loader
import requests
# Create your views here.
def index(request):
    query = request.GET.get('q')

    if query:
        url = 'http://www.omdbapi.com/?apikey=682238fb&s=' + query
        response = requests.get(url)
        movie_data = response.json()

        context = {
            'query':query,
            'movie_data':movie_data
        }

        template = loader.get_template('search-resault.html')

        return HttpResponse(template.render(context,request))
    return render(request,'index.html')    