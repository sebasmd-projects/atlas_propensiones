# Generated by Django 4.2.7 on 2024-12-28 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets_location', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assetlocationmodel',
            name='observations',
        ),
        migrations.AddField(
            model_name='assetlocationmodel',
            name='observations_en',
            field=models.TextField(blank=True, null=True, verbose_name='observations (EN)'),
        ),
        migrations.AddField(
            model_name='assetlocationmodel',
            name='observations_es',
            field=models.TextField(blank=True, null=True, verbose_name='observations (ES)'),
        ),
    ]
