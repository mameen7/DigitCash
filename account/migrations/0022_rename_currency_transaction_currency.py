# Generated by Django 3.2.9 on 2022-01-03 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0021_alter_wallet_currency'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='Currency',
            new_name='currency',
        ),
    ]
