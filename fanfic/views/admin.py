from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from fanfic.forms import EditFicForm
from fanfic.models import Fic


def FicEditingView(request, pk):
    fic_to_edit = get_object_or_404(Fic, pk=pk)

    if request.method == 'POST':
        form = EditFicForm(request.POST)

        if form.is_valid():
            fic_to_edit.fic_title = form.cleaned_data['fic_title']
            fic_to_edit.save()
            fic_id = fic_to_edit.id

            # redirect to the edited fic because why not:
            return HttpResponseRedirect(reverse('fanfic:index'))
    else:
        original_title = fic_to_edit.fic_title
        form = EditFicForm(initial={'fic_title': original_title})

    return render(request,
                  'admin/fic-edit.html',
                  {'form': form,
                   'fic_to_edit': fic_to_edit})
