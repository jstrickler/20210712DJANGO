# Generated by Django 3.0 on 2021-05-12 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djpres_core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='president',
            name='termnum',
        ),
    ]
