"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from references import views as st_views

urlpatterns = [

    #Authors URLs

    path("admin/", admin.site.urls),
    path('author_preview/<int:pk>/', st_views.ShowAuthor.as_view(), name='author_detail'),
    path('author_create/', st_views.CreateAuthor.as_view(), name='author_create'),
    path('author_update/<int:pk>/', st_views.UpdateAuthor.as_view(), name='author_update'),
    path('author_delete/<int:pk>/', st_views.DeleteAuthor.as_view(), name='author_delete'),
    path('authors_list/', st_views.ShowAuthors.as_view(), name='authors_list'),

    #Series URLs

    path('series_preview/<int:pk>/', st_views.ShowSeries.as_view(), name='series_detail'),
    path('series_create/', st_views.CreateSeries.as_view(), name='series_create'),
    path('series_update/<int:pk>/', st_views.UpdateSeries.as_view(), name='series_update'),
    path('series_delete/<int:pk>/', st_views.DeleteSeries.as_view(), name='series_delete'),
    path('all_series_list/', st_views.ShowAllSeries.as_view(), name='series_list'),

    #Genres URLs

    path('genre_preview/<int:pk>/', st_views.ShowGenre.as_view(), name='genre_detail'),
    path('genre_create/', st_views.CreateGenre.as_view(), name='genre_create'),
    path('genre_update/<int:pk>/', st_views.UpdateGenre.as_view(), name='genre_update'),
    path('genre_delete/<int:pk>/', st_views.DeleteGenre.as_view(), name='genre_delete'),
    path('genres_list/', st_views.ShowGenres.as_view(), name='genres_list'),

    #Publishing houses URLs

    path('house_preview/<int:pk>/', st_views.ShowHouse.as_view(), name='house_detail'),
    path('house_create/', st_views.CreateHouse.as_view(), name='house_create'),
    path('house_update/<int:pk>/', st_views.UpdateHouse.as_view(), name='house_update'),
    path('house_delete/<int:pk>/', st_views.DeleteHouse.as_view(), name='house_delete'),
    path('houses_list/', st_views.ShowHouses.as_view(), name='houses_list')
]
