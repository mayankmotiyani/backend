# Generated by Django 4.0.5 on 2022-08-10 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about_company', '0015_buildconnection'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buildconnection',
            old_name='description',
            new_name='content',
        ),
    ]
