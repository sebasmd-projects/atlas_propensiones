# Generated by Django 4.2.21 on 2025-07-05 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pol', '0002_rename_proofoflife_proofoflifemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proofoflifemodel',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='proofoflifemodel',
            name='second_last_name',
        ),
    ]
