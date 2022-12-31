# Generated by Django 4.1.4 on 2022-12-31 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_orderitem_com'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='com',
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='is_paid',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
