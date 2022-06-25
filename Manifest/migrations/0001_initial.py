# Generated by Django 4.0.3 on 2022-06-25 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataStructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.BooleanField(default=False)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DS_Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('reviewer', models.CharField(max_length=20, null=True)),
                ('remark', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manifest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=7)),
                ('personal_wo', models.TextField(default='', null=True)),
                ('misc_wo', models.TextField(default='', null=True)),
                ('technical_score', models.IntegerField(default=0, null=True)),
                ('misc_score', models.IntegerField(default=0, null=True)),
                ('is_complete', models.BooleanField(default=False)),
                ('next_review', models.DateField(null=True)),
                ('folder', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskname', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.BooleanField(default=False)),
                ('created', models.DateField(auto_now_add=True)),
                ('week', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Manifest.manifest')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('remark', models.TextField(default='', null=True)),
                ('status', models.CharField(choices=[('Task Completed', 'Task Completed'), ('Need Improvement', 'Need Improvement'), ('Task Critical', 'Task Critical'), ('Repeat Review', 'Repeat Review')], default='', max_length=20)),
                ('advisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.advisor')),
                ('manifest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manifest.manifest')),
                ('reviewer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.reviewer')),
            ],
        ),
    ]
