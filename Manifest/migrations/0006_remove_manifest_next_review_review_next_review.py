# Generated by Django 4.0.3 on 2022-05-18 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manifest', '0005_alter_datastructure_userid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manifest',
            name='next_review',
        ),
        migrations.AddField(
            model_name='review',
            name='next_review',
            field=models.DateTimeField(null=True),
        ),
    ]
