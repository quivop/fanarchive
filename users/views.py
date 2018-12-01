from .forms import FicUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SignUp(CreateView):
    form_class = FicUserCreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'