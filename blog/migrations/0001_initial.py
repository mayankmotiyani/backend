# Generated by Django 4.0.4 on 2022-07-27 11:15

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='blogTitle')),
                ('description', models.TextField(blank=True, null=True, verbose_name='blogDescription')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='blogContent')),
                ('image', models.ImageField(upload_to='blog', verbose_name='blogImage')),
                ('slug', models.SlugField(blank=True, max_length=500, verbose_name='blogSlug')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creationDate')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updatedDate')),
            ],
            options={
                'verbose_name_plural': 'Blog',
            },
        ),
    ]
