from django.shortcuts import render

# import to enable super-simple pages
from django.http import HttpResponse

# import to enable DYNAMIC NEW index page
from .models import Work, WorkPart

# importing get_object_or_404 shortcut function
from django.shortcuts import get_object_or_404

# DYNAMIC NEW index page
def index(request):
	# get the five latest works
	latest_work_list = Work.objects.order_by('-date_created')[:5]
	
	# pass latest works to a variable
	the_works = {'latest_work_list': latest_work_list,}

	# render latest works using index.jinja template and the latest_work_list variable
	return render(request, 'fanarchive/index.jinja', the_works)

# DYNAMIC detail page
def detail(request, work_id):
	# which will give you a 404 if the work you're trying to look up doesn't exist
	work = get_object_or_404(Work, pk=work_id)
	return render(request, 'fanarchive/detail.jinja', {'work': work})

# super simple 'whole work' page
def whole_work(request, work_id):
	return HttpResponse("You're looking at ALL PARTS of work %s" % work_id)