from django.contrib import admin
from catalog.models import AppUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, MyUserCreationForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = MyUserCreationForm
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ("username", "email", "name", "surname", "phone")
    # list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': (
            "username", 
            "email", 
            "name", 
            "surname", 
            "phone", 
            "country", 
            "city", 
            "index", 
            "address", 
            "reserve_address", 
            "password",
            "additional_info"
        )}),
        ('Status', {'fields': (
            'is_staff', 
            'is_superuser', 
            'is_active'
        )}),
        ('Permissions', {'fields': (
            'groups', 
            'user_permissions'
        )}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                "username", 
                "email", 
                "name", 
                "surname", 
                "phone", 
                "country", 
                "city", 
                "index", 
                "address", 
                "reserve_address", 
                "password1", 
                "password2", 
                "additional_info"
            ),
        }),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()

admin.site.register(AppUser, UserAdmin)