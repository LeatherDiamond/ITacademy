from . import models, forms
from django.shortcuts import render
from django.views import generic

# Create your views here.

class ShowAuthors(generic.ListView):
    model = models.BookAuthor
    template_name = 'references/list_author.html'


class ShowAuthor(generic.DetailView):
    model = models.BookAuthor
    template_name = 'references/detail_author.html'


class CreateAuthor(generic.CreateView):
    model = models.BookAuthor
    form_class = forms.AuthorForm
    template_name = 'references/create_author.html'


class UpdateAuthor(generic.UpdateView):
    model = models.BookAuthor
    form_class = forms.AuthorForm
    template_name = 'references/update_author.html'


class DeleteAuthor(generic.DeleteView):
    model = models.BookAuthor
    template_name = 'references/delete_author.html'
    def get_success_url(self):
        return ('/authors_list/')
