from django.shortcuts import render
from django.views import generic
from product_card.models import Book


# Create your views here.

class HomePage(generic.TemplateView):
    template_name = 'home_page/home_page.html'

#PK manually made for deployed database
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['new_book'] = Book.objects.get(pk=3)
        context['awesome_book'] = Book.objects.get(pk=10)
        context['history_book'] = Book.objects.get(pk=2)
        return context