# Generated by Django 3.1.7 on 2021-02-19 22:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0002_auto_20210219_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 19, 22, 1, 39, 348333, tzinfo=utc)),
        ),
    ]
