# Generated by Django 4.0.5 on 2022-08-02 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_rename_process_developmentprocess_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhatWeDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='whatWeDoTitle')),
                ('content', models.TextField(verbose_name='whatWeDoContent')),
                ('image', models.ImageField(upload_to='what_we_do', verbose_name='whatWeDoImage')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creationDate')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updatedDate')),
            ],
            options={
                'verbose_name_plural': 'What We Do',
            },
        ),
    ]