# Generated by Django 4.0 on 2022-01-18 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0008_gateway_huashu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gateway',
            name='huashu',
            field=models.ManyToManyField(to='words.Word', verbose_name='话术'),
        ),
    ]