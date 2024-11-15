# Generated by Django 4.2.7 on 2024-11-15 23:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('certificates', '0004_remove_certificatemodel_step'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificatemodel',
            name='approval_date',
            field=models.DateField(blank=True, null=True, verbose_name='Approval date'),
        ),
        migrations.AddField(
            model_name='certificatemodel',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='approved_certificates', to=settings.AUTH_USER_MODEL, verbose_name='Approved by'),
        ),
    ]
