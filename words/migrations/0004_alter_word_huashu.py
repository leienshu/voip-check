# Generated by Django 4.0 on 2022-01-18 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_account_created_at_account_updated_at'),
        ('words', '0003_word_created_at_word_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='huashu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account', verbose_name='关联用户'),
        ),
    ]
