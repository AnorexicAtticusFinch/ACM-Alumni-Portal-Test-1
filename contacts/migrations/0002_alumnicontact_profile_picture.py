# Generated by Django 3.0.5 on 2020-04-16 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnicontact',
            name='profile_picture',
            field=models.FileField(blank=True, default='./images/genericdp.jpg', upload_to='uploads/%Y/%m/%d'),
        ),
    ]
