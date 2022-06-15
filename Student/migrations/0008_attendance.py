# Generated by Django 4.0.4 on 2022-06-13 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0007_student_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('student', models.ManyToManyField(to='Student.student')),
            ],
        ),
    ]
