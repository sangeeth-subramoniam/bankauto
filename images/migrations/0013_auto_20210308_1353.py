# Generated by Django 3.1.7 on 2021-03-08 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0012_auto_20210308_1334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='updimagestext',
            old_name='updimages',
            new_name='updimage',
        ),
    ]
