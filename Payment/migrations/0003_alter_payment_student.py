# Generated by Django 4.0.3 on 2022-05-18 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0003_alter_shifted_student'),
        ('Payment', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Student.student'),
        ),
    ]