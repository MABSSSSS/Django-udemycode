# Generated by Django 5.0.9 on 2024-09-23 05:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PayRollApp', '0005_rename_location_department_locationname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='EmpCountry',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='Countries', to='PayRollApp.country'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='EmpDepartment',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='Department', to='PayRollApp.department'),
        ),
    ]
