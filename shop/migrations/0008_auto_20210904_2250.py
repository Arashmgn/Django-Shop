# Generated by Django 3.2.6 on 2021-09-04 18:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20210904_2139'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'سفارش', 'verbose_name_plural': 'سفارشات'},
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 4, 18, 20, 32, 477734, tzinfo=utc), verbose_name='تاریخ ثبت'),
        ),
    ]
