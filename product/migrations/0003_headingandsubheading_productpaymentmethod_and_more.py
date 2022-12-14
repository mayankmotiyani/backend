# Generated by Django 4.0.5 on 2022-08-04 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeadingAndSubheading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subheading', models.CharField(max_length=500, verbose_name='homepageSubheading')),
                ('heading', models.TextField(blank=True, null=True, verbose_name='homepageHeading')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creationDate')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updatedDate')),
            ],
            options={
                'verbose_name_plural': 'Heading & Subheading',
            },
        ),
        migrations.CreateModel(
            name='ProductPaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='productPaymentMethodTitle')),
                ('content', models.TextField(verbose_name='productPaymentMethodContent')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creationDate')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updatedDate')),
                ('heading', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.headingandsubheading')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductFunctionality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='productFunctionalitytitle')),
                ('content', models.TextField(verbose_name='productFunctionalitycontent')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creationDate')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updatedDate')),
                ('heading', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.headingandsubheading')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='OurGoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='productGoalTitle')),
                ('content', models.TextField(verbose_name='productGoalContent')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creationDate')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updatedDate')),
                ('heading', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.headingandsubheading')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'verbose_name_plural': 'Our Goal',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='heading',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.headingandsubheading'),
        ),
    ]
