# Generated by Django 4.0.5 on 2022-08-01 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blockchain',
            name='blockchain_description',
            field=models.TextField(blank=True, null=True, verbose_name='blockchainDescription'),
        ),
    ]