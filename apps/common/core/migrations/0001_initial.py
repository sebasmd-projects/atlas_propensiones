# Generated by Django 4.2.7 on 2024-11-29 03:16

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, choices=[('es', 'Spanish'), ('en', 'English')], default='es', max_length=4, null=True, verbose_name='language')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('default_order', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='priority')),
                ('unique_id', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('last_name', models.CharField(max_length=255, verbose_name='last name')),
                ('email', models.EmailField(max_length=255, verbose_name='email')),
                ('subject', models.CharField(max_length=255, verbose_name='subject')),
                ('message', models.TextField(verbose_name='message')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
                'db_table': 'apps_core_contact',
            },
        ),
    ]
