# Generated by Django 5.0.9 on 2024-09-23 06:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PayRollApp', '0006_alter_employee_empcountry_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='EmpDepartment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Department', to='PayRollApp.department'),
        ),
    ]
