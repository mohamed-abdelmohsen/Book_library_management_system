# Generated by Django 4.2.5 on 2023-10-06 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_alter_borrowedbook_return_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='image',
            field=models.ImageField(null=True, upload_to='book/images'),
        ),
    ]