# Generated by Django 4.0.5 on 2022-08-09 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0018_alter_herosection_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='headingandsubheading',
            name='description',
            field=models.TextField(default='', verbose_name='description'),
        ),
    ]
