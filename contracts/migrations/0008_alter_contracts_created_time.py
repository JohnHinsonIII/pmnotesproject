# Generated by Django 4.1.3 on 2022-12-02 17:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0007_alter_contracts_created_time_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contracts',
            name='created_time',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 12, 2, 11, 59, 59, 475175)),
        ),
    ]
