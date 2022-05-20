# Generated by Django 4.0.3 on 2022-05-18 12:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Batch', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='code',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='batch',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='batch',
            name='location',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
