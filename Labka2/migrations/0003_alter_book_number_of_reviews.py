# Generated by Django 4.1.6 on 2023-03-30 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Labka2', '0002_alter_book_publication_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='number_of_reviews',
            field=models.IntegerField(null=True),
        ),
    ]
