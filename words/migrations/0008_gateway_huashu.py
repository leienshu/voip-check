# Generated by Django 4.0 on 2022-01-18 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0007_remove_gateway_huashu'),
    ]

    operations = [
        migrations.AddField(
            model_name='gateway',
            name='huashu',
            field=models.ManyToManyField(to='words.Word'),
        ),
    ]