# Generated by Django 2.0.5 on 2018-10-04 21:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 5, 3, 24, 41, 505444)),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 5, 3, 24, 41, 504447), null=True),
        ),
    ]