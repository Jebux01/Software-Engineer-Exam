# Generated by Django 3.0.5 on 2021-06-30 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_order_date_up'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='subtotal',
        ),
    ]
