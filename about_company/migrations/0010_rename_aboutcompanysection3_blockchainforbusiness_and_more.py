# Generated by Django 4.0.5 on 2022-08-10 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about_company', '0009_headingandsubheading_description_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AboutCompanySection3',
            new_name='BlockchainForBusiness',
        ),
        migrations.RenameModel(
            old_name='AboutCompanySection1',
            new_name='UnmatchedServices',
        ),
        migrations.AlterModelOptions(
            name='blockchainforbusiness',
            options={'verbose_name_plural': 'Blockchain For Business'},
        ),
        migrations.AlterModelOptions(
            name='unmatchedservices',
            options={'verbose_name_plural': '8+ Years of unmatched Services'},
        ),
    ]