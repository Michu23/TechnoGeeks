# Generated by Django 4.0.3 on 2022-06-01 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manifest', '0006_remove_manifest_next_review_review_next_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='next_review',
        ),
        migrations.AddField(
            model_name='manifest',
            name='next_review',
            field=models.DateTimeField(null=True),
        ),
    ]
