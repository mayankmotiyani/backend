# Generated by Django 4.0.5 on 2022-08-04 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_alter_headingandsubheading_heading'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='whatwedo',
            name='heading_and_subheading',
        ),
        migrations.AddField(
            model_name='whatwedo',
            name='heading',
            field=models.CharField(max_length=250, null=True, verbose_name='whatWeDoHeading'),
        ),
    ]
