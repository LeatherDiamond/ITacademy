from django.urls import path
from . import views

app_name = "catalog"
urlpatterns = [
    path('', views.Catalog.as_view(), name='catalog'),
]