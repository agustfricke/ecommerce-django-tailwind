# Generated by Django 4.1.4 on 2022-12-31 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_orderitem_is_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='is_paid',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
