# Generated by Django 4.0.5 on 2022-07-29 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=250, verbose_name='fullName')),
                ('email', models.EmailField(max_length=250, verbose_name='emailId')),
                ('contactNumber', models.CharField(max_length=100, verbose_name='contactNumber')),
                ('countryName', models.CharField(max_length=100, verbose_name='countryName')),
                ('projectDescription', models.TextField(default='', help_text='PROJECT DESCRIPTION', verbose_name='projectDescription')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creationDate')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updatedDate')),
            ],
            options={
                'verbose_name_plural': 'Contact Infograins',
            },
        ),
    ]
