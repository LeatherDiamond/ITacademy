from django.shortcuts import render
from django.views import generic
from product_card.models import Book


# Create your views here.


class Catalog(generic.TemplateView):
    template_name = 'catalog/catalog.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['book1'] = Book.objects.get(pk=1)
        context['book2'] = Book.objects.get(pk=2)
        context['book3'] = Book.objects.get(pk=3)
        context['book4'] = Book.objects.get(pk=4)
        context['book5'] = Book.objects.get(pk=5)
        context['book6'] = Book.objects.get(pk=6)
        context['book7'] = Book.objects.get(pk=7)
        context['book8'] = Book.objects.get(pk=8)
        context['book9'] = Book.objects.get(pk=9)
        context['book10'] = Book.objects.get(pk=10)
        return context