# Generated by Django 4.1.3 on 2022-12-03 21:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0020_alter_clinreport_created_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinreport',
            name='created_time',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 12, 3, 16, 20, 16, 268676)),
        ),
        migrations.AlterField(
            model_name='contracts',
            name='created_time',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 12, 3, 16, 20, 16, 266673)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='created_time',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 12, 3, 16, 20, 16, 268676)),
        ),
        migrations.AlterField(
            model_name='laborposition',
            name='created_time',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 12, 3, 16, 20, 16, 268676)),
        ),
    ]