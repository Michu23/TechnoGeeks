# Generated by Django 4.0.4 on 2022-06-20 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Batch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Placement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(blank=True, max_length=20, null=True)),
                ('company', models.CharField(blank=True, max_length=30, null=True)),
                ('location', models.CharField(blank=True, max_length=20, null=True)),
                ('LPA', models.FloatField()),
                ('count', models.IntegerField(null=True)),
                ('created', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shifted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Training', 'Training'), ('Placed', 'Placed'), ('RequestedTermination', 'RequestedTermination'), ('Terminated', 'Terminated'), ('Quit', 'Quit')], max_length=20)),
                ('fee', models.CharField(choices=[('Upfront', 'Upfront'), ('ISI', 'ISI')], default='ISI', max_length=20)),
                ('batch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Batch.batch')),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Batch.branch')),
            ],
        ),
    ]
