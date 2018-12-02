from django import forms
from authtools.forms import UserCreationForm, UserChangeForm
from .models import FicUser


class FicUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = FicUser
        fields = ('name', 'email')


class FicUserChangeForm(UserChangeForm):

    class Meta:
        model = FicUser
        fields = ('name', 'email')
