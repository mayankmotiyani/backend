# Generated by Django 4.0.5 on 2022-08-01 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=500, null=True, verbose_name='slug'),
        ),
    ]
