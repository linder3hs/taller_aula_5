# Generated by Django 4.1.3 on 2022-12-02 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_book_average_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='num_pages',
            field=models.CharField(max_length=200),
        ),
    ]
