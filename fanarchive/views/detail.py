from django.views import generic

from fanarchive.models import Work, WorkPart

class DetailView(generic.DetailView):
	model = Work
	template_name = 'fanarchive/detail.jinja'
