# Generated by Django 4.0.5 on 2022-08-04 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_remove_herosection_heading_and_subheading_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headingandsubheading',
            name='heading',
            field=models.TextField(blank=True, null=True, verbose_name='homepageHeading'),
        ),
    ]
