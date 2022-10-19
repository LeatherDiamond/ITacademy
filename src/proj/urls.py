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
    path('author_preview/<int:pk>/', st_views.ShowAuthor.as_view()),
    path('author_create/', st_views.CreateAuthor.as_view()),
    path('author_update/<int:pk>/', st_views.UpdateAuthor.as_view()),
    path('author_delete/<int:pk>/', st_views.DeleteAuthor.as_view()),
    path('authors_list/', st_views.ShowAuthors.as_view()),

    #Series URLs

    path('series_preview/<int:pk>/', st_views.ShowSeries.as_view()),
    path('series_create/', st_views.CreateSeries.as_view()),
    path('series_update/<int:pk>/', st_views.UpdateSeries.as_view()),
    path('series_delete/<int:pk>/', st_views.DeleteSeries.as_view()),
    path('all_series_list/', st_views.ShowAllSeries.as_view()),

    #Genres URLs

    path('genre_preview/<int:pk>/', st_views.ShowGenre.as_view()),
    path('genre_create/', st_views.CreateGenre.as_view()),
    path('genre_update/<int:pk>/', st_views.UpdateGenre.as_view()),
    path('genre_delete/<int:pk>/', st_views.DeleteGenre.as_view()),
    path('genres_list/', st_views.ShowGenres.as_view()),

    #Publishing houses URLs

    path('house_preview/<int:pk>/', st_views.ShowHouse.as_view()),
    path('house_create/', st_views.CreateHouse.as_view()),
    path('house_update/<int:pk>/', st_views.UpdateHouse.as_view()),
    path('house_delete/<int:pk>/', st_views.DeleteHouse.as_view()),
    path('houses_list/', st_views.ShowHouses.as_view())
]
