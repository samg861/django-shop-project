# Generated by Django 4.2.3 on 2023-09-02 11:28

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
