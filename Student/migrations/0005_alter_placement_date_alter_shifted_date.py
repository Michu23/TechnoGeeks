# Generated by Django 4.0.3 on 2022-06-01 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0004_placement_count_placement_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placement',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='shifted',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]