# Generated by Django 3.0.5 on 2021-06-30 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_order_subtotal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='dateCanceled',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='dateCompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='dateDelivered',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='dateInProcess',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]