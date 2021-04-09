# Generated by Django 3.1.7 on 2021-04-08 13:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0003_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='authot',
            new_name='author',
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 8, 13, 49, 36, 352361, tzinfo=utc)),
        ),
    ]
