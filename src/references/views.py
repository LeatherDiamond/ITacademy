from . import models, forms
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.

#CBV for Author model.

class ShowAuthors(generic.ListView):
    model = models.BookAuthor
    template_name = 'references/list_author.html'


class ShowAuthor(generic.DetailView):
    model = models.BookAuthor
    template_name = 'references/detail_author.html'


class CreateAuthor(generic.CreateView):
    model = models.BookAuthor
    form_class = forms.AuthorForm
    template_name = 'references/edit_author.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context


class UpdateAuthor(generic.UpdateView):
    model = models.BookAuthor
    form_class = forms.AuthorForm
    template_name = 'references/edit_author.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context


class DeleteAuthor(generic.DeleteView):
    model = models.BookAuthor
    template_name = 'references/delete_author.html'

    def get_success_url(self):
        return reverse_lazy('authors_list')

#CBV for Series model.

class ShowAllSeries(generic.ListView):
    model = models.BookSeries
    template_name = 'references/list_series.html'


class ShowSeries(generic.DetailView):
    model = models.BookSeries
    template_name = 'references/detail_series.html'


class CreateSeries(generic.CreateView):
    model = models.BookSeries
    form_class = forms.SeriesForm
    template_name = 'references/edit_series.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context


class UpdateSeries(generic.UpdateView):
    model = models.BookSeries
    form_class = forms.SeriesForm
    template_name = 'references/edit_series.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context


class DeleteSeries(generic.DeleteView):
    model = models.BookSeries
    template_name = 'references/delete_series.html'

    def get_success_url(self):
        return reverse_lazy('series_list')

#CBV for Genre model.

class ShowGenres(generic.ListView):
    model = models.BookGenre
    template_name = 'references/list_genre.html'


class ShowGenre(generic.DetailView):
    model = models.BookGenre
    template_name = 'references/detail_genre.html'


class CreateGenre(generic.CreateView):
    model = models.BookGenre
    form_class = forms.GenreForm
    template_name = 'references/edit_genre.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context


class UpdateGenre(generic.UpdateView):
    model = models.BookGenre
    form_class = forms.GenreForm
    template_name = 'references/edit_genre.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context


class DeleteGenre(generic.DeleteView):
    model = models.BookGenre
    template_name = 'references/delete_genre.html'

    def get_success_url(self):
        return reverse_lazy('genres_list')

#CBV Publishing house form.

class ShowHouses(generic.ListView):
    model = models.BookPublishingHouse
    template_name = 'references/list_house.html'


class ShowHouse(generic.DetailView):
    model = models.BookPublishingHouse
    template_name = 'references/detail_house.html'


class CreateHouse(generic.CreateView):
    model = models.BookPublishingHouse
    form_class = forms.PublishingHouseForm
    template_name = 'references/edit_house.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context


class UpdateHouse(generic.UpdateView):
    model = models.BookPublishingHouse
    form_class = forms.PublishingHouseForm
    template_name = 'references/edit_house.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context


class DeleteHouse(generic.DeleteView):
    model = models.BookPublishingHouse
    template_name = 'references/delete_house.html'

    def get_success_url(self):
        return reverse_lazy('houses_list')