from django.views import generic

from fanarchive.models import Work


class DetailView(generic.DetailView):
    model = Work
    template_name = 'fanarchive/detail.html'
