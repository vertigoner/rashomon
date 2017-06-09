import urllib.request
import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def home(request):
	return render(request, 'db/home.html')

def search(request):
	query = request.GET.get('search_box')
	response = urllib.request.urlopen("http://www.omdbapi.com/?t=" + query).read().decode('utf8')
	parsed_response = json.loads(response)
	title = parsed_response['Title']
	director = parsed_response['Director']

	context = {'title' : title, 'director' : director}
	return render(request, 'db/search.html', context)

	#return HttpResponse(response)