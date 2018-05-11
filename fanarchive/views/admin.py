from django.http import HttpResponse
from django.shortcuts import get_object_or_404


from fanarchive.forms import EditFicForm
from fanarchive.models import Fic


def FicEditingView(request):
    return HttpResponse("This will be a form. someday...")
