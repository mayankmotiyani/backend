# Generated by Django 4.0.5 on 2022-08-05 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0008_dummysection2_heading_dummysection3_heading_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dummysection2',
            name='heading',
        ),
        migrations.RemoveField(
            model_name='dummysection3',
            name='heading',
        ),
        migrations.RemoveField(
            model_name='ourunparalleledservice',
            name='heading',
        ),
    ]
