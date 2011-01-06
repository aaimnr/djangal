from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from djang.galeria.models import Dywan
import webalbum
def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")
def dywan(request, dywan_id):
	d = get_object_or_404(Dywan, pk=dywan_id)
	return render_to_response('dywan.html',{'dywan':d})
	
	
def albumy(request):
	client = webalbum.getAuthClient()
	albsData = webalbum.getAlbumsData(client)
	#return HttpResponse(albsData[0])
	return render_to_response('albumy.html', {'albsData':albsData})
	
def album(request, album_id):
	ht=webalbum.getPhotosHtml(album_id)
	return HttpResponse(ht)
	
def galeria(request):
	ht=webalbum.getPhotosHtml()
	return HttpResponse(ht)
	
	
	