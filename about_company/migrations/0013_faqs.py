# Generated by Django 4.0.5 on 2022-08-10 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_company', '0012_alter_blockchainforbusiness_image_visionandmission_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('question', models.TextField(blank=True, null=True, verbose_name='question')),
                ('answer', models.TextField(blank=True, null=True, verbose_name='answer')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creationDate')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updatedDate')),
            ],
            options={
                'verbose_name_plural': 'FAQ',
            },
        ),
    ]