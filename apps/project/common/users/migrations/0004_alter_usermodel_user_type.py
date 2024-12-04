# Generated by Django 4.2.13 on 2024-12-03 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_usermodel_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='user_type',
            field=models.CharField(choices=[('I', 'Intermediary'), ('H', 'Holder'), ('B', 'Buyer'), ('A', 'Representative')], default='H', max_length=2, verbose_name='User'),
        ),
    ]