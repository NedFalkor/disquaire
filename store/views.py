from django.shortcuts import render
from django.http import HttpResponse

from .models import ALBUMS

def index(request):
    message = "Hello"
    return HttpResponse(message)

def listing(request): 
    albums = ["<li>{}</li>".format(albums['name']) for albums in ALBUMS]
    message = """<ul>{}</ul>""".format("\n".join(albums))
    return HttpResponse(message)

def detail(request, album_id):
    id = int(album_id)
    album = ALBUMS[id]
    artists = " ".join([artist['name'] for artist in album['artists']])
    message = "Le nom de l'album est {}. Il a été écrit par {}".format(album['name'], artists)
    return HttpResponse(message)

def search(request):
    obj = str(request.GET)
    query = request.GET['query']
    message = "propriété GET : {} et requête : {}".format(obj,query)
    return HttpResponse(message)