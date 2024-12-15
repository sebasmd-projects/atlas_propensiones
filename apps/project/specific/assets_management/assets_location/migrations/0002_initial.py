# Generated by Django 4.2.7 on 2024-12-15 06:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assets_location', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationmodel',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assetslocation_location_user', to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='assetlocationmodel',
            name='asset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assetlocation_assetlocation_asset', to='assets.assetmodel', verbose_name='Asset'),
        ),
        migrations.AddField(
            model_name='assetlocationmodel',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assetslocation_assetslocation_user', to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AddField(
            model_name='assetlocationmodel',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assetlocation_assetlocation_location', to='assets_location.locationmodel', verbose_name='location'),
        ),
        migrations.AlterUniqueTogether(
            name='assetcountrymodel',
            unique_together={('continent', 'es_country_name', 'en_country_name')},
        ),
        migrations.AlterUniqueTogether(
            name='locationmodel',
            unique_together={('reference', 'country', 'created_by', 'is_active')},
        ),
        migrations.AlterUniqueTogether(
            name='assetlocationmodel',
            unique_together={('asset', 'location', 'quantity_type', 'amount', 'created_by', 'is_active')},
        ),
    ]
