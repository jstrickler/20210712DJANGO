# Generated by Django 3.0.6 on 2021-07-14 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wombats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wombat',
            name='sex',
            field=models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=1, null=True),
        ),
    ]
