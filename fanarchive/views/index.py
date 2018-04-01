from django.views import generic

from fanarchive.models import Work, WorkPart

class IndexView(generic.ListView):
	template_name = 'fanarchive/index.html'
	context_object_name = 'latest_work_list'

	def get_queryset(self):
		"""Return the last five published works"""
		return Work.objects.order_by('-date_created')[:5]