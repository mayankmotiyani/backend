# Generated by Django 4.0.5 on 2022-07-30 09:11

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blockchain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blockchain_name', models.CharField(default='', max_length=250, verbose_name='blockchainName')),
                ('blockchain_slug', models.SlugField(blank=True, default='', max_length=250, null=True, verbose_name='blockchainSlug')),
                ('blockchain_content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='blockchainContent')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creationDate')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updatedDate')),
            ],
            options={
                'verbose_name_plural': 'Blockchain',
            },
        ),
        migrations.CreateModel(
            name='BlockchainCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blockchain_category', models.CharField(max_length=100, verbose_name='blockchainCategory')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creationDate')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updatedDate')),
            ],
            options={
                'verbose_name_plural': 'Blockchain Category',
            },
        ),
        migrations.CreateModel(
            name='BlockchainService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blockchain_service_name', models.CharField(max_length=250, verbose_name='blockchainServiceName')),
                ('blockchain_service_slug', models.SlugField(blank=True, default='', max_length=250, null=True, verbose_name='blockchainServiceSlug')),
                ('blockchain_content', models.TextField(blank=True, default='', null=True, verbose_name='blockchainContent')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creationDate')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updatedDate')),
                ('blockchain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blockchain.blockchain')),
            ],
            options={
                'verbose_name_plural': 'Blockchain Service',
            },
        ),
        migrations.AddField(
            model_name='blockchain',
            name='blockchainCategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blockchain.blockchaincategory'),
        ),
    ]