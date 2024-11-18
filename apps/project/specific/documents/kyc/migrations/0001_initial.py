# Generated by Django 4.2.13 on 2024-11-16 21:16

from django.db import migrations, models
import django.utils.timezone
import encrypted_model_fields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LegalAdvisorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, choices=[('es', 'Spanish'), ('en', 'English')], default='es', max_length=4, null=True, verbose_name='language')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('default_order', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='priority')),
                ('legal_advisor_first_name', models.CharField(max_length=100, verbose_name='Legal Advisor Name')),
                ('legal_advisor_last_name', models.CharField(max_length=100, verbose_name='Legal Advisor Last Name')),
                ('legal_advisor_card_id', encrypted_model_fields.fields.EncryptedCharField(verbose_name='Legal Advisor Card ID')),
                ('legal_advisor_country', models.CharField(max_length=100, verbose_name='Legal Advisor Country')),
                ('legal_advisor_phonenumber', encrypted_model_fields.fields.EncryptedCharField(verbose_name='Legal Advisor Phone Number')),
                ('legal_advisor_email', encrypted_model_fields.fields.EncryptedEmailField(verbose_name='Legal Advisor Email')),
            ],
            options={
                'verbose_name': 'Legal Advisor',
                'verbose_name_plural': 'Legal Advisors',
                'db_table': 'apps_project_specific_documents_kyc_legal_advisor',
            },
        ),
    ]
