from django import forms


class EditFicForm(forms.form):
    fic_title = forms.CharField(help_text="Enter a shiny new title for your fanfic (default is original title).")
