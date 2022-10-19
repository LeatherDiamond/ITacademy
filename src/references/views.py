from . import models, forms
from django.shortcuts import render
from django.views import generic

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
    template_name = 'references/create_series.html'


class UpdateSeries(generic.UpdateView):
    model = models.BookSeries
    form_class = forms.SeriesForm
    template_name = 'references/update_series.html'


class DeleteSeries(generic.DeleteView):
    model = models.BookSeries
    template_name = 'references/delete_series.html'


    def get_success_url(self):
        return ('/all_series_list/')

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
    template_name = 'references/create_genre.html'


class UpdateGenre(generic.UpdateView):
    model = models.BookGenre
    form_class = forms.GenreForm
    template_name = 'references/update_genre.html'


class DeleteGenre(generic.DeleteView):
    model = models.BookGenre
    template_name = 'references/delete_genre.html'


    def get_success_url(self):
        return ('/genres_list/')

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
    template_name = 'references/create_house.html'


class UpdateHouse(generic.UpdateView):
    model = models.BookPublishingHouse
    form_class = forms.PublishingHouseForm
    template_name = 'references/update_house.html'


class DeleteHouse(generic.DeleteView):
    model = models.BookPublishingHouse
    template_name = 'references/delete_house.html'

    
    def get_success_url(self):
        return ('/houses_list/')