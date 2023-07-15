# Generated by Django 4.2 on 2023-06-25 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoMedicalApp', '0009_alter_bill_id_alter_company_id_alter_customer_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billdetails',
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
        migrations.AlterField(
            model_name='customerrequest',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employeebank',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employeesalary',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
