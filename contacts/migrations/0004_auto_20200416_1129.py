# Generated by Django 3.0.5 on 2020-04-16 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20200416_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnicontact',
            name='profile_picture',
            field=models.FileField(blank=True, default='../images/genericdp.jpg', null=True, upload_to='uploads/%Y/%m/%d'),
        ),
    ]
