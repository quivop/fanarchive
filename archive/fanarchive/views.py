from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# adding this to power switch to generic views
from django.views import generic

from .models import Work, WorkPart

class IndexView(generic.ListView):
	template_name = 'fanarchive/index.jinja'
	context_object_name = 'latest_work_list'

	def get_queryset(self):
		"""Return the last five published works"""
		return Work.objects.order_by('-date_created')[:5]

class DetailView(generic.DetailView):
	model = Work
	template_name = 'fanarchive/detail.jinja'
