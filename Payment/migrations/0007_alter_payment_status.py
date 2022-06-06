# Generated by Django 4.0.4 on 2022-06-06 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0006_payment_totalamt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Expired', 'Expired'), ('Partially', 'Partially')], max_length=10),
        ),
    ]
