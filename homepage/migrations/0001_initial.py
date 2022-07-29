# Generated by Django 4.0.4 on 2022-07-27 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeroSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='title')),
                ('content', models.TextField(verbose_name='content')),
                ('image', models.ImageField(upload_to='hero_section_images', verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creationDate')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updatedDate')),
            ],
            options={
                'verbose_name_plural': 'Hero Section',
            },
        ),
        migrations.CreateModel(
            name='NotableBlockchainPlatforms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('image', models.ImageField(upload_to='notable_blockchain_platforms', verbose_name='image')),
                ('content', models.TextField(verbose_name='content')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creationDate')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updatedDate')),
            ],
            options={
                'verbose_name_plural': 'High-End Expertise In Blockchain',
            },
        ),
        migrations.CreateModel(
            name='OurMastery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='nichesName')),
                ('image', models.ImageField(upload_to='niche_images', verbose_name='nicheImages')),
                ('content', models.TextField(verbose_name='nicheContent')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creationDate')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updatedDate')),
            ],
            options={
                'verbose_name_plural': 'Our Mastery',
            },
        ),
    ]
