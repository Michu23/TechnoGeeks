# Generated by Django 4.0.3 on 2022-06-16 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0014_merge_20220616_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='Media/Profile/defaultProPic.png', upload_to='Media/Profile'),
        ),
    ]