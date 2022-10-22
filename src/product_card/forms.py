from django import forms
from . import models


class ProductCardForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = ['name', 'image', 'author', 'price', 'series', 'genre', 'publishing_year', 'pages', 'binding',\
         'format', 'isbn', 'weight', 'age_restriction', 'publishing_house', 'available_books', 'activity', \
         'rating', 'date_of_addition'
         ]
    

