# Generated by Django 4.2.13 on 2024-12-03 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyers', '0004_offermodel_offer_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offermodel',
            name='offer_amount',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=20, verbose_name='Offer Amount per quantity type in USD'),
        ),
    ]