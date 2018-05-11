from django.http import HttpResponse

from .forms import EditFicForm


def FicEditView(request):
    return HttpResponse("This will be a form. someday...")
