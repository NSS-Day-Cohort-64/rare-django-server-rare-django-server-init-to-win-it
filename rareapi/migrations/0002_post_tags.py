# Generated by Django 4.2.4 on 2023-08-30 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='rareapi.tag'),
        ),
    ]
