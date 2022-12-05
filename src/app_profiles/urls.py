from django.urls import path
from . import views

app_name = 'app_profiles'
urlpatterns = [
    path('profile_view/<int:pk>', views.ProfileView.as_view(), name='profile_view'),
    path('cancel_order/', views.CancelOrderView.as_view(), name="cancel_order"),
]