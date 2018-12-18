from .forms import FicUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from authtools.views import PasswordResetView


class SignUp(CreateView):
    form_class = FicUserCreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'


class ResetView(PasswordResetView):
    template_name = 'users/password_reset.html'
    subject_template_name = 'users/password_reset_subject.txt'
    email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')