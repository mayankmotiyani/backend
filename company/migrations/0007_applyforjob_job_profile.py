# Generated by Django 4.0.5 on 2022-08-05 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_remove_applyforjob_skill_set'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyforjob',
            name='job_profile',
            field=models.CharField(max_length=250, null=True, verbose_name='jobProfile'),
        ),
    ]