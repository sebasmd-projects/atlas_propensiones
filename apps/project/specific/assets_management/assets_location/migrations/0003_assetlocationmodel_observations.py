# Generated by Django 4.2.7 on 2024-12-16 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets_location', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetlocationmodel',
            name='observations',
            field=models.TextField(blank=True, null=True, verbose_name='observations'),
        ),
    ]