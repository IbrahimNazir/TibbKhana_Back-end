# Generated by Django 4.2 on 2023-06-25 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoMedicalApp', '0015_alter_company_id_alter_companyaccount_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='companyaccount',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='companybank',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]