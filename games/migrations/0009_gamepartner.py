# Generated by Django 4.0.5 on 2022-08-10 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0008_headingandsubheading_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='GamePartner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='game_partners')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creationDate')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updatedDate')),
                ('heading', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.headingandsubheading')),
            ],
            options={
                'verbose_name_plural': 'Game Partners',
            },
        ),
    ]