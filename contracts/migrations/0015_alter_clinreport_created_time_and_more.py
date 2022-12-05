# Generated by Django 4.1.3 on 2022-12-02 22:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0014_alter_clinreport_created_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinreport',
            name='created_time',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 12, 2, 17, 48, 37, 576990)),
        ),
        migrations.AlterField(
            model_name='contracts',
            name='created_time',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 12, 2, 17, 48, 37, 574997)),
        ),
        migrations.AlterField(
            model_name='document',
            name='attach_file',
            field=models.FileField(blank=True, null=True, upload_to='contract-attachments/'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='created_time',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 12, 2, 17, 48, 37, 576990)),
        ),
        migrations.AlterField(
            model_name='laborposition',
            name='created_time',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 12, 2, 17, 48, 37, 575994)),
        ),
    ]
