# Generated by Django 3.0.5 on 2020-08-22 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20200821_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reporter',
            name='email',
        ),
        migrations.RemoveField(
            model_name='reporter',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='reporter',
            name='last_name',
        ),
    ]
