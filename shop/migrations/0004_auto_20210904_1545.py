# Generated by Django 3.2.6 on 2021-09-04 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0003_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('s', 'ارسال شده'), ('p', 'در حال پردازش'), ('r', 'رسیده به دست مشتری')], default='در حال پردازش', max_length=1, verbose_name='وضعیت سفارش'),
        ),
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(blank='true', max_length=200, verbose_name='قیمت کل'),
        ),
        migrations.AlterField(
            model_name='order',
            name='costumer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نام مشتری'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='تاریخ ثبت'),
        ),
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.CharField(max_length=1000, verbose_name='محصولات'),
        ),
    ]