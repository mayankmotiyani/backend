# Generated by Django 4.0.5 on 2022-07-30 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NFT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='NftName')),
                ('slug', models.SlugField(blank=True, max_length=250, null=True, verbose_name='NftSlug')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creationDate')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updatedDate')),
            ],
            options={
                'verbose_name_plural': 'NFT',
            },
        ),
    ]