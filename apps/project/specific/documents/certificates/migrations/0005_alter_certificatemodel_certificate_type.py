# Generated by Django 4.2.7 on 2025-01-08 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0004_certificatetypesmodel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificatemodel',
            name='certificate_type',
            field=models.ForeignKey(blank=True, default='IDONEITY', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='certificates_certificate_certificate_type', to='certificates.certificatetypesmodel', verbose_name='Certificate type'),
        ),
    ]
