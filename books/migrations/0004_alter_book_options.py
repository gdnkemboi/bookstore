# Generated by Django 4.2.4 on 2023-08-05 07:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0003_book_cover"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="book",
            options={"permissions": [("special_status", "Can read all books")]},
        ),
    ]
