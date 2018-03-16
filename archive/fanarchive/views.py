from django.shortcuts import render

# import to enable super-simple index page
from django.http import HttpResponse

# super-simple index page
def index(request):
	return HttpResponse("Hello, cruel fanfic world. You are at the fanarchive index.")
