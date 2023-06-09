from django.shortcuts import render

from .models import TitleFilm

def index(request):
    titles = TitleFilm.objects.order_by('title')
    context= { 'titles': titles }
    return render(request, 'films_app/index.html', context)

