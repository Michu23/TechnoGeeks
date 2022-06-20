# Generated by Django 4.0.3 on 2022-06-19 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0016_remove_profile_domain'),
        ('Student', '0021_remove_shifted_shifted_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='domain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='User.domain'),
        ),
        migrations.AddField(
            model_name='student',
            name='fee',
            field=models.CharField(choices=[('Upfront', 'Upfront'), ('ISI', 'ISI')], default='ISI', max_length=20),
        ),
    ]