# Generated by Django 4.1.3 on 2022-11-29 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='Category_name',
            new_name='category_name',
        ),
    ]
