# Generated by Django 4.0.5 on 2022-08-04 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_product_heading'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='aboutProductTitle')),
                ('content', models.TextField(verbose_name='aboutProductContent')),
                ('image', models.ImageField(upload_to='about_product', verbose_name='aboutProductImage')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creationDate')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updatedDate')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
