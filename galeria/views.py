from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from djang.galeria.models import Dywan
def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")
def dywan(request, dywan_id):
	d = get_object_or_404(Dywan, pk=dywan_id)
	return render_to_response('dywan.html',{'dywan':d})