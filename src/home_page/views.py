from django.shortcuts import render, redirect
from django.views import generic
from product_card.models import Book
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group


# Create your views here.

#User logout

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

#User authentication

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username, password)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                next_param = request.POST.get('next')
                if next_param:
                    url = next_param
                else:
                    url = '/'
                return HttpResponseRedirect(url)
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="home_page/login.html", context={"login_form":form})

#User create view

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            group = Group.objects.get(name='Customers')
            user.groups.add(group)
            next_param = request.POST.get('next')
            if next_param:
                url = next_param
            else:
                url = '/'
            return HttpResponseRedirect(url)
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="home_page/register.html", context={"register_form":form})


#PK manually made for deployed database

class HomePage(generic.TemplateView):
    template_name = 'home_page/home_page.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['new_book'] = Book.objects.get(pk=3) 
        context['awesome_book'] = Book.objects.get(pk=10)
        context['history_book'] = Book.objects.get(pk=2)
        return context


class ShippingInfo(generic.TemplateView):
    template_name = 'home_page/shipping_info.html'


class AboutCompany(generic.TemplateView):
    template_name = 'home_page/about_info.html'