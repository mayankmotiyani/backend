# Generated by Django 4.0.5 on 2022-08-05 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_alter_applyforjob_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applyforjob',
            name='skill_set',
        ),
    ]
