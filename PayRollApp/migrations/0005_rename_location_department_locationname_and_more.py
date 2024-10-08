# Generated by Django 5.0.9 on 2024-09-23 05:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PayRollApp', '0004_country_department'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='Location',
            new_name='LocationName',
        ),
        migrations.AddField(
            model_name='employee',
            name='EmpCountry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='PayRollApp.country'),
        ),
        migrations.AddField(
            model_name='employee',
            name='EmpDepartment',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='PayRollApp.department'),
        ),
    ]
