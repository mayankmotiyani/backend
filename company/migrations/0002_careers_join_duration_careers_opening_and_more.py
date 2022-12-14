# Generated by Django 4.0.5 on 2022-08-02 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='careers',
            name='join_duration',
            field=models.CharField(blank=True, help_text='for example : 15 Days, 30 Days', max_length=250, null=True, verbose_name='joinDuration'),
        ),
        migrations.AddField(
            model_name='careers',
            name='opening',
            field=models.IntegerField(blank=True, null=True, verbose_name='openingVacancy'),
        ),
        migrations.AddField(
            model_name='careers',
            name='opening_available',
            field=models.BooleanField(default=True, verbose_name='isAvailable'),
        ),
        migrations.AlterField(
            model_name='careers',
            name='location',
            field=models.CharField(default='Indore', max_length=250, null=True, verbose_name='location'),
        ),
    ]
