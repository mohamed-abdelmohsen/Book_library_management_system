# Generated by Django 4.2.5 on 2023-10-06 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_books_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrowedbook',
            old_name='borrower',
            new_name='user',
        ),
    ]
