# Generated by Django 4.0.4 on 2022-06-02 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0008_alter_profile_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
    ]
