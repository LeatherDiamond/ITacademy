from django.shortcuts import (
    get_object_or_404,
    render,
)
from django.views import generic

from catalog.models import AppUser
from order.models import Order


# Create your views here.


class ProfileView(generic.DetailView):

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(AppUser, pk=kwargs['pk'])
        return render(
            request, 'app_profiles/profile_view.html', context={
                'user': user,
                'orders': Order.objects.select_related('cart').filter(user=request.user),
            }
        )


class CancelOrderView(generic.DeleteView):
    template_name = 'app_profiles/order_view.html'
    model = Order

     
