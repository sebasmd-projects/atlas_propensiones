# Generated by Django 4.2.7 on 2025-01-02 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_usermodel_is_verified_holder'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='citizenship_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Citizenship Number'),
        ),
    ]
