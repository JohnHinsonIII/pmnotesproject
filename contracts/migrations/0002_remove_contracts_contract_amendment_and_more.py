# Generated by Django 4.1.3 on 2022-12-01 15:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contracts',
            name='contract_amendment',
        ),
        migrations.RemoveField(
            model_name='contracts',
            name='contract_nda',
        ),
        migrations.RemoveField(
            model_name='contracts',
            name='contract_renewal',
        ),
        migrations.AlterField(
            model_name='contracts',
            name='created_time',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 12, 1, 10, 10, 46, 727625)),
        ),
    ]
