# Generated by Django 5.0.6 on 2024-07-06 15:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modul', '0003_alter_user_uid_alter_usertg_last_interaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.BigIntegerField(default=4907543697, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='usertg',
            name='last_interaction',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 7, 6, 15, 59, 46, 710300, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
