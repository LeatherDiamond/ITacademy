from django.shortcuts import render
from django.views import generic, View
from product_card.models import Book
from django.core.paginator import Paginator

# Create your views here.


class CatalogView(View):

    def get(self, request, *args, **kwargs):
        book = Book.objects.all()
        paginator = Paginator(book, 12)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            'catalog/catalog.html',
            context={
                'page_obj': page_obj
            }
        )


class BookDetail(generic.TemplateView):
    template_name = 'catalog/book_detail.html'

    def get_context_data(self, *args, **kwargs):
        pk = kwargs['pk']    
        context = super().get_context_data(*args, **kwargs)
        context['pk'] = Book.objects.get(pk=pk)
        return context
