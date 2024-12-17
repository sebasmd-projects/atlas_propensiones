# Generated by Django 4.2.7 on 2024-12-17 05:57

import apps.project.specific.assets_management.assets.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssetCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, choices=[('es', 'Spanish'), ('en', 'English')], default='es', max_length=4, null=True, verbose_name='language')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('default_order', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='priority')),
                ('es_name', models.CharField(max_length=50, verbose_name='category (ES)')),
                ('en_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='category (EN)')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': '2. Category',
                'verbose_name_plural': '2. Categories',
                'db_table': 'apps_assets_assetcategory',
                'ordering': ['default_order', '-created'],
            },
        ),
        migrations.CreateModel(
            name='AssetsNamesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, choices=[('es', 'Spanish'), ('en', 'English')], default='es', max_length=4, null=True, verbose_name='language')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('default_order', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='priority')),
                ('es_name', models.CharField(max_length=255, verbose_name='asset (es)')),
                ('en_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='asset (en)')),
            ],
            options={
                'verbose_name': '3. Asset Name',
                'verbose_name_plural': '3. Asset Names',
                'db_table': 'apps_assets_assetsnames',
                'ordering': ['default_order', '-created'],
            },
        ),
        migrations.CreateModel(
            name='AssetModel',
            fields=[
                ('language', models.CharField(blank=True, choices=[('es', 'Spanish'), ('en', 'English')], default='es', max_length=4, null=True, verbose_name='language')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('default_order', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='priority')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('asset_img', models.ImageField(blank=True, max_length=255, null=True, upload_to=apps.project.specific.assets_management.assets.models.AssetModel.assets_directory_path, verbose_name='img')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('observations', models.TextField(blank=True, default='', null=True, verbose_name='observations')),
                ('asset_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assets_asset_assetsnames', to='assets.assetsnamesmodel', verbose_name='asset')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assets_asset_assetcategory', to='assets.assetcategorymodel', verbose_name='category')),
            ],
            options={
                'verbose_name': '1. Asset',
                'verbose_name_plural': '1. Assets',
                'db_table': 'apps_assets_asset',
                'ordering': ['default_order', '-created'],
                'unique_together': {('asset_name', 'category')},
            },
        ),
    ]
