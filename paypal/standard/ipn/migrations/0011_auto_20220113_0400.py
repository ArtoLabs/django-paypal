# Generated by Django 3.2.11 on 2022-01-13 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipn', '0010_auto_20220113_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paypalipn',
            name='cart_list_ids',
            field=models.CharField(blank=True, default='', max_length=512),
        ),
        migrations.AlterField(
            model_name='paypalipn',
            name='cart_list_qtys',
            field=models.CharField(blank=True, default='', max_length=512),
        ),
        migrations.AlterField(
            model_name='paypalipn',
            name='cart_list_shipping_costs',
            field=models.CharField(blank=True, default='', max_length=512),
        ),
    ]
