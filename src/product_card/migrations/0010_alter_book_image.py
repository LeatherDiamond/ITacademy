# Generated by Django 4.1.1 on 2022-10-25 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product_card", "0009_alter_book_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="uploads/%Y/%m/%d/",
                verbose_name="Book image",
            ),
        ),
    ]