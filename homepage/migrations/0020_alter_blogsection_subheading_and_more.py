# Generated by Django 4.0.5 on 2022-08-09 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0019_headingandsubheading_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogsection',
            name='subheading',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='blogSubheading'),
        ),
        migrations.AlterField(
            model_name='startsomethingundeniably',
            name='subheading',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='subHeading'),
        ),
    ]
