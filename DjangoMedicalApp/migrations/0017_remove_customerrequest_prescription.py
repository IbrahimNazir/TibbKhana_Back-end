# Generated by Django 4.2 on 2023-07-13 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoMedicalApp', '0016_alter_company_id_alter_companyaccount_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerrequest',
            name='prescription',
        ),
    ]
