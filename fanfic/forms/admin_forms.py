from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class EditFicForm(forms.Form):
    fic_title = forms.CharField(help_text="Enter a shiny new title for your fanfic (default is original title).")

    def clean_fic_title(self):
        data = self.cleaned_data['fic_title']

        # Check title is not longer than 200 characters
        if len(data) > 200:
            raise ValidationError(_('Title is too long - fic title must be 200 characters or less in length'))

        return data


class NewUserForm(forms.Form):
    pass
