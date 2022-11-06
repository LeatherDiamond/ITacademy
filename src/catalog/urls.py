from django.urls import path
from . import views

app_name = "catalog"
urlpatterns = [
    path('all_books/', views.Catalog.as_view(), name='catalog'),
]