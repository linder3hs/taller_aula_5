# Generated by Django 4.1.3 on 2022-12-01 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0007_book_bookid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='bookID',
        ),
    ]
