# Generated by Django 4.0.3 on 2022-06-16 13:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0027_alter_payment_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='expiry_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 6, 15, 19, 9, 2, 22887), null=True),
        ),
    ]