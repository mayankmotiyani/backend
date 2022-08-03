# Generated by Django 4.0.5 on 2022-08-03 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_modernsolutionforvariousplatform_delete_gamecontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameSection3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='GameTitle')),
                ('image', models.ImageField(upload_to='game', verbose_name='image')),
                ('content', models.TextField(verbose_name='GameContent')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creationDate')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updatedDate')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.game')),
            ],
        ),
        migrations.CreateModel(
            name='GameSection2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='GameTitle')),
                ('image', models.ImageField(upload_to='game', verbose_name='image')),
                ('content', models.TextField(verbose_name='GameContent')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creationDate')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updatedDate')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.game')),
            ],
        ),
    ]
