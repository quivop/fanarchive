from django.views import generic

from fanfic.models import Fic


class IndexView(generic.ListView):
    template_name = 'fanfic/index.html'
    context_object_name = 'latest_fic_list'

    def get_queryset(self):
        """Return the last five published fics"""
        return Fic.objects.order_by('-pub_date')[:5]
