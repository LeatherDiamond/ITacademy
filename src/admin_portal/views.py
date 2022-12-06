from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from order.models import (
    Order,
    Status,
)
from django.http import (
    HttpResponseRedirect,
)
from django.shortcuts import (
    get_object_or_404,
    render,
)
from django.urls import reverse_lazy
from django.views import generic
from admin_portal.forms import PortalForm

# Create your views here.

class AdminPortalView(LoginRequiredMixin, PermissionRequiredMixin, generic.TemplateView):
    permission_required = 'product_card.view_book'
    login_url = 'admin_portal:admin_portal'

    def get(self, request, *args, **kwargs):
        return render(
            request, 'admin_portal/portal_detail.html', context={
                'user': request.user,
                'orders': Order.objects.select_related('cart'),
            }
        )

    
    # def post(self, request, *args, **kwargs):
    #     form = PortalForm(request.POST, instance=request.order)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(reverse_lazy('admin_portal/portal_detail.html'))
    #     return render(
    #         request, 'admin_portal/portal_detail.html', context={
    #             'user': request.user,
    #             'orders': Order.objects.select_related('cart'),
    #             'form': form,
    #         }
    #     )


class StatusView(generic.UpdateView):
    def post(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        order = get_object_or_404(Order, pk=pk)
        status = self.request.POST.get('status')
        order.status = status
        order.save()
        return HttpResponseRedirect(reverse_lazy('admin_portal/portal_detail.html'))
