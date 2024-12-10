# Generated by Django 4.2.7 on 2024-12-06 06:24

from django.db import migrations, models
import django.utils.timezone
import encrypted_model_fields.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CertificateModel',
            fields=[
                ('language', models.CharField(blank=True, choices=[('es', 'Spanish'), ('en', 'English')], default='es', max_length=4, null=True, verbose_name='language')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('default_order', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='priority')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Names')),
                ('last_name', models.CharField(default='', max_length=100, verbose_name='Last name')),
                ('document_type', models.CharField(choices=[('CC', 'Citizen ID (CC)'), ('CE', 'Foreigner ID (CE)'), ('PPT', 'Special Residence Permit (PPT)'), ('TI', 'Identity Card (TI)'), ('PA', 'Passport (PA)'), ('RC', 'Civil Registry (RC)'), ('NIT', 'Tax Identification Number (NIT)'), ('RUT', 'Single Tax Registry (RUT)'), ('CD', 'Diplomatic ID Card (CD)')], default='CC', max_length=4, verbose_name='Document type')),
                ('document_number', encrypted_model_fields.fields.EncryptedCharField(verbose_name='Document number')),
                ('document_number_hash', models.CharField(default='', editable=False, max_length=64)),
                ('approved', models.BooleanField(default=True, verbose_name='Approved')),
                ('approval_date', models.DateField(blank=True, null=True, verbose_name='Approval date')),
            ],
            options={
                'verbose_name': 'Certificate',
                'verbose_name_plural': 'Certificates',
                'db_table': 'apps_certificates_certificate',
                'ordering': ['default_order', '-created'],
                'permissions': [('view_certificate', 'Can view certificate list')],
            },
        ),
    ]
