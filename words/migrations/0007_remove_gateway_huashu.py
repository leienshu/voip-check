# Generated by Django 4.0 on 2022-01-18 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0006_gateway'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gateway',
            name='huashu',
        ),
    ]
