# Generated by Django 3.0.5 on 2020-08-21 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200820_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporter',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
