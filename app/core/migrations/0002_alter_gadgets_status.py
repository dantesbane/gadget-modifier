# Generated by Django 4.2.17 on 2025-01-27 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gadgets',
            name='status',
            field=models.CharField(choices=[('Available', 'Active'), ('Unavailable', 'Inactive'), ('Destroyed', 'Destroyed'), ('Decommissioned', 'Decommissioned')], default='Available'),
        ),
    ]
