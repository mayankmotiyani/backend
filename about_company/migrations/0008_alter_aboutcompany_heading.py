# Generated by Django 4.0.5 on 2022-08-09 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_company', '0007_aboutcompanysection3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutcompany',
            name='heading',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
