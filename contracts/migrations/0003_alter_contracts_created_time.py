# Generated by Django 4.1.3 on 2022-12-01 18:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0002_remove_contracts_contract_amendment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contracts',
            name='created_time',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 12, 1, 13, 27, 10, 473359)),
        ),
    ]