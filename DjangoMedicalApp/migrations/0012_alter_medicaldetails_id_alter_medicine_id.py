# Generated by Django 4.2 on 2023-06-25 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoMedicalApp', '0011_alter_medicaldetails_id_alter_medicine_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicaldetails',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
