# Generated by Django 4.2.5 on 2023-10-06 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_rename_borrower_borrowedbook_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowedbook',
            name='borrow_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]