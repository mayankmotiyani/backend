# Generated by Django 4.0.5 on 2022-08-01 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DevelopmentProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process', models.CharField(max_length=500, verbose_name='blockchainProcessTitle')),
                ('content', models.TextField(verbose_name='blockchainProcessContent')),
                ('image', models.ImageField(upload_to='blockchain_process', verbose_name='blockchainProcessImage')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creationDate')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updatedDate')),
            ],
            options={
                'verbose_name_plural': 'Blockchain Development Process',
            },
        ),
    ]
