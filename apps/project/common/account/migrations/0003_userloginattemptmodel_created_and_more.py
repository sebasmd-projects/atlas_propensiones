# Generated by Django 4.2.7 on 2024-11-14 22:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userloginattemptmodel',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='userloginattemptmodel',
            name='default_order',
            field=models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='priority'),
        ),
        migrations.AddField(
            model_name='userloginattemptmodel',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is active'),
        ),
        migrations.AddField(
            model_name='userloginattemptmodel',
            name='language',
            field=models.CharField(blank=True, choices=[('es', 'Spanish'), ('en', 'English')], default='es', max_length=4, null=True, verbose_name='language'),
        ),
        migrations.AddField(
            model_name='userloginattemptmodel',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='updated'),
        ),
    ]
