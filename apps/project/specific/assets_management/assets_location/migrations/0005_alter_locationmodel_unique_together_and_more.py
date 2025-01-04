# Generated by Django 4.2.7 on 2024-12-28 01:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assets_location', '0004_alter_assetlocationmodel_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='locationmodel',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='locationmodel',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='description (EN)'),
        ),
        migrations.AddField(
            model_name='locationmodel',
            name='description_es',
            field=models.TextField(blank=True, null=True, verbose_name='description (ES)'),
        ),
        migrations.AlterUniqueTogether(
            name='locationmodel',
            unique_together={('reference', 'country', 'created_by', 'is_active', 'description_es', 'description_en')},
        ),
        migrations.RemoveField(
            model_name='locationmodel',
            name='description',
        ),
    ]