# Generated by Django 4.0.5 on 2022-08-01 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='latest',
            field=models.BooleanField(default=False, null=True, verbose_name='latestBlog'),
        ),
    ]
