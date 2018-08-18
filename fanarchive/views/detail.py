from django.views import generic

from fanarchive.models import Fic


class DetailView(generic.DetailView):
    model = Fic
    template_name = 'fanarchive/detail.html'