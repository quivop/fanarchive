from django.shortcuts import render

# import to enable super-simple index page
from django.http import HttpResponse

# super-simple index page
def index(request):
	# now with Jinja2~
	return render(request, 'fanarchive/index.jinja')

# super simple detail page
def detail(request, work_id):
	return HttpResponse("You're looking at work %s" % work_id)

# super simple 'whole work' page
def whole_work(request, work_id):
	return HttpResponse("You're looking at ALL PARTS of work %s" % work_id)