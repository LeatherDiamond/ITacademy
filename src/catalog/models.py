from django.db import models
from django.utils import timezone
from product_card.models import Book
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin

# Create your models here.

class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             related_name='comments')
    username = models.ForeignKey('AppUser', on_delete=models.CASCADE,
                                 related_name='user_name')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_date']

        def __str__(self):
            return self.text


class AppUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        unique=True,
        max_length=30,
    )
    email = models.EmailField(blank=True, null=True)

    is_staff = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_superuser = models.BooleanField(
        default=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = 'username'
        verbose_name_plural = 'usernames'
        abstract = False