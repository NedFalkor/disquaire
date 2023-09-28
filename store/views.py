from django.shortcuts import render
from django.http import HttpResponse

from .models import Album, Artist, Contact, Booking

def index(request):
    Album.objects.filter(available=True).order_by('-created_at') [:12]
    message = "Hello"
    return HttpResponse(message)

def listing(request): 
    albums = ["<li>{}</li>".format(albums.title) for albums in Album]
    message = """<ul>{}</ul>""".format("\n".join(albums))
    return HttpResponse(message)

def detail(request, album_id):
    album = Album.objects.get(pk=album_id)
    artists = " ".join([artist.name for artist in album.artists.all()])
    message = "Le nom de l'album est {}. Il a été écrit par {}".format(album.title, artists)
    return HttpResponse(message)

def search(request):
    query = request.GET.get('query')
    if not query:
        albums = Album.objects.all()
    else:
        albums = Album.objects.filter(title_icontains=query)
        
        if not albums.exists():
            albums = Album.objects.filter(artists_name_icontains=query)
        else:
            albums = ["<li>{}</li>".format(albums['name']) for albums in albums]
            message = """nous avons trouvé ceci ! : 
                <ul>
                {}
                </ul>""".format("\n".join(albums))
    return HttpResponse(message)
