# Generated by Django 5.2.3 on 2025-06-28 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='likes',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
