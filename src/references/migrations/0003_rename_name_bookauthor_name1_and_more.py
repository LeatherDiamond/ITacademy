# Generated by Django 4.1.1 on 2022-10-08 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("references", "0002_alter_bookauthor_name_alter_bookauthor_surname"),
    ]

    operations = [
        migrations.RenameField(
            model_name="bookauthor", old_name="name", new_name="name1",
        ),
        migrations.RenameField(
            model_name="bookauthor", old_name="surname", new_name="surname1",
        ),
        migrations.AddField(
            model_name="bookauthor",
            name="name2",
            field=models.CharField(
                blank=True, max_length=30, null=True, verbose_name="Author's name"
            ),
        ),
        migrations.AddField(
            model_name="bookauthor",
            name="surname2",
            field=models.CharField(
                blank=True, max_length=30, null=True, verbose_name="Author's name"
            ),
        ),
    ]