from django.shortcuts import render
from django.views import generic
from catalog.models import AppUser
from carts.models import Cart, BooksInCart
from order.models import Order
from django.shortcuts import get_object_or_404, render

# Create your views here.


class ProfileView(generic.DetailView):


    def get(self, request, *args, **kwargs):
        user = get_object_or_404(AppUser, pk=kwargs['pk'])
        return render(request, 'app_profiles/profile_view.html', context={
            'user': user,
            'order': Order.objects.filter(user=request.user),
        })    


class OrderView(generic.DetailView):
    login_url = 'home_page:login'
    template_name = 'app_profiles/order_view.html'
    model = Order


