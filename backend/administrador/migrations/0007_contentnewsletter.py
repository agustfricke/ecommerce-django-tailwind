# Generated by Django 4.1.4 on 2022-12-31 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0006_remove_newsletter_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentNewsLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
            ],
        ),
    ]
