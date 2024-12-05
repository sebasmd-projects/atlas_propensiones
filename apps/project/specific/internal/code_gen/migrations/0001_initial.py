# Generated by Django 4.2.7 on 2024-12-05 03:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodeRegistrationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, choices=[('es', 'Spanish'), ('en', 'English')], default='es', max_length=4, null=True, verbose_name='language')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('default_order', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='priority')),
                ('reference', models.CharField(max_length=100, verbose_name='Reference')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('custom_text_input', models.CharField(blank=True, max_length=100, null=True, verbose_name='Custom Text Input')),
                ('code_information', models.TextField(blank=True, null=True, verbose_name='Code Information')),
            ],
            options={
                'verbose_name': 'Code Registration',
                'verbose_name_plural': 'Code Registrations',
                'db_table': 'apps_code_gen_coderegistration',
            },
        ),
    ]
