# Generated by Django 4.0.4 on 2022-06-12 07:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0017_alter_payment_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='expiry_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 6, 11, 12, 46, 20, 419440), null=True),
        ),
    ]