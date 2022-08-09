# Generated by Django 4.0.5 on 2022-08-08 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0013_contactinformation_getintouch_alter_partner_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(default='', max_length=250, verbose_name='clientName')),
                ('client_feedback', models.TextField(default='', verbose_name='clientFeedback')),
                ('image', models.ImageField(null=True, upload_to='testimonials', verbose_name='clientImage')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creationDate')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updatedDate')),
            ],
            options={
                'verbose_name_plural': 'Testimonials',
                'ordering': ['id'],
            },
        ),
    ]