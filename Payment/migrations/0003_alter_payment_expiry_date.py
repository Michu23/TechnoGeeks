# Generated by Django 4.0.5 on 2022-06-20 10:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='expiry_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 6, 19, 16, 9, 31, 119079), null=True),
        ),
    ]