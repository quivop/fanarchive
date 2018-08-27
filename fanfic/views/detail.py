from django.views import generic

from fanfic.models import Fic


class DetailView(generic.DetailView):
    model = Fic
    template_name = 'fanfic/detail.html'