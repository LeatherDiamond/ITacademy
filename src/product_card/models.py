from django.db import models
from references.models import BookAuthor
from references.models import BookSeries
from references.models import BookGenre
from references.models import BookPublishingHouse

# Create your models here.


class Book(models.Model):
    name = models.CharField(
       max_length = 30,
       verbose_name="Book name"
    )
    image = models.ImageField(
    )
    author = models.ManyToManyField(
        BookAuthor,
        verbose_name="Author/Authors",
    )
    price = models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        verbose_name="Price"
    )
    series = models.ManyToManyField(
        BookSeries,
        verbose_name="Series",
    )
    genre = models.ManyToManyField(
        BookGenre,
        verbose_name="Genre",
    )
    publishing_year=models.CharField(
        max_length=11,
        verbose_name="Publishing year"
    )
    pages = models.IntegerField(
        verbose_name="Pages"
    )
    binding = models.CharField(
        max_length=30,
        verbose_name="Binding"
    )
    format = models.CharField(
        max_length=7,
        verbose_name="Format"
    )
    isbn = models.CharField(
        max_length=30,
        verbose_name="ISBN"
    )
    weight = models.IntegerField( 
        verbose_name="Weight"
    )
    age_restriction = models.IntegerField( 
        verbose_name="Age restriction"
    )
    publishing_house = models.ManyToManyField(
        BookPublishingHouse,
        verbose_name="Publishing house/Publishing houses"
    )
    available_books = models.IntegerField(
        verbose_name="Available books"
    )
    activity = models.CharField(
        max_length = 3,
        verbose_name="Avaliability"
    )
    rating = models.DecimalField(
        max_digits=2, 
        decimal_places=1,
        verbose_name="Rating"
    )
    date_of_addition = models.DateField(
        verbose_name="Date of addition"
    )
    modification_date = models.DateTimeField(
        auto_now=True,
        verbose_name="Modification date"
    )
