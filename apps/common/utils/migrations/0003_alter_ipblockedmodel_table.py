# Generated by Django 4.2.7 on 2024-11-11 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0002_requestlogmodel'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='ipblockedmodel',
            table='apps_common_utils_ipblocked',
        ),
    ]
