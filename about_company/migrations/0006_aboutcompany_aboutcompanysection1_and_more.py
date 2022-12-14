# Generated by Django 4.0.5 on 2022-08-05 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about_company', '0005_privacypolicy_title_termsandcondition_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='aboutCompany')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creationDate')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updatedDate')),
            ],
            options={
                'verbose_name_plural': 'About Company',
            },
        ),
        migrations.CreateModel(
            name='AboutCompanySection1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='aboutCompany')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creationDate')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updatedDate')),
            ],
            options={
                'verbose_name_plural': 'About Company Section 1',
            },
        ),
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
        migrations.DeleteModel(
            name='About',
        ),
        migrations.AddField(
            model_name='aboutcompanysection1',
            name='heading',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about_company.headingandsubheading'),
        ),
        migrations.AddField(
            model_name='aboutcompany',
            name='heading',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about_company.headingandsubheading'),
        ),
    ]
