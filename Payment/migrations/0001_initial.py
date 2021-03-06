# Generated by Django 4.0.5 on 2022-06-25 09:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(blank=True, default=0, null=True)),
                ('paid', models.IntegerField(blank=True, default=0, null=True)),
                ('upi', models.IntegerField(blank=True, default=0, null=True)),
                ('cash', models.IntegerField(blank=True, default=0, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Expired', 'Expired'), ('Partially', 'Partially')], max_length=10)),
                ('types', models.CharField(choices=[('CautionDeposit', 'CautionDeposit'), ('Rent', 'Rent'), ('BatchShift', 'BatchShift'), ('Upfront', 'Upfront')], max_length=20)),
                ('date', models.DateField(default=datetime.date.today)),
                ('totalamt', models.IntegerField(blank=True, default=0, null=True)),
                ('month', models.CharField(choices=[('---', '---'), ('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], default='---', max_length=20)),
                ('paid_date', models.DateField(blank=True, null=True)),
                ('expiry_date', models.DateField(blank=True, default=datetime.datetime(2022, 6, 24, 14, 37, 17, 586800), null=True)),
                ('paymentid', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
    ]
