# Generated by Django 4.0.4 on 2022-06-13 07:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0021_alter_payment_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='expiry_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 6, 12, 12, 56, 39, 559563), null=True),
        ),
    ]