# Generated by Django 4.0.4 on 2022-06-26 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='govtid',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]