# Generated by Django 3.0.5 on 2020-08-21 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]