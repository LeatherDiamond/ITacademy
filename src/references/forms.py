from django import forms
from . import models


class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.BookAuthor
        fields = ['name', 'surname', 'description']


   