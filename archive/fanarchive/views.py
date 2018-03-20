from django.shortcuts import render

# import to enable super-simple pages
from django.http import HttpResponse

# import to enable DYNAMIC NEW index page
from .models import Work

# DYNAMIC NEW index page
def index(request):
	# get the five latest works
	latest_work_list = Work.objects.order_by('-date_created')[:5]
	
	# pass latest works to a variable
	the_works = {'latest_work_list': latest_work_list,}

	# render latest works using index.jinja template and the latest_work_list variable
	return render(request, 'fanarchive/index.jinja', the_works)

# super simple detail page
def detail(request, work_id):
	return HttpResponse("You're looking at work %s" % work_id)

# super simple 'whole work' page
def whole_work(request, work_id):
	return HttpResponse("You're looking at ALL PARTS of work %s" % work_id)