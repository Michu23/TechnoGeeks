# Generated by Django 4.0.4 on 2022-06-20 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Student', '0001_initial'),
        ('Payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Student.student'),
        ),
    ]
