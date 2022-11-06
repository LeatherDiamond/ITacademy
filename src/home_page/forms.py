from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    index = forms.IntegerField(required=True)
    name = forms.CharField(required=True, max_length=30)
    surname = forms.CharField(required=True, max_length=30)
    phone = forms.IntegerField(required=True, help_text="Enter the number in international format.")
    country = forms.CharField(required=True)
    city = forms.CharField(required=True, max_length=30)
    address = forms.CharField(required=True, max_length=60)
    reserve_address = forms.CharField(required=False, max_length=60)
    additional_info = forms.CharField(required=False, max_length=150)

    class Meta:
        model = User
        fields = ("username", "email", "name", "surname", "phone", "country", "city", "index", "address", "reserve_address",  "password1", "password2", "additional_info")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.name = self.cleaned_data['name']
        user.surname = self.cleaned_data['surname']
        user.country = self.cleaned_data['country']
        user.city = self.cleaned_data['city']
        user.index = self.cleaned_data['index']
        user.address = self.cleaned_data['address']
        user.reserve_address = self.cleaned_data['reserve_address']
        user.additional_info = self.cleaned_data['additional_info']
        if commit:
            user.save()
        return user