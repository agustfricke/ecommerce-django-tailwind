# Generated by Django 4.1.4 on 2022-12-31 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='com',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
