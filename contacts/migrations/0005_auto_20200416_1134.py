# Generated by Django 3.0.5 on 2020-04-16 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20200416_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnicontact',
            name='profile_picture',
            field=models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d'),
        ),
    ]