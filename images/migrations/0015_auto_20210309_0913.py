# Generated by Django 3.1.7 on 2021-03-09 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0014_auto_20210309_0910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='updimagestext',
            name='updimage',
        ),
        migrations.AddField(
            model_name='updimages',
            name='link',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='images.updimagestext'),
        ),
    ]