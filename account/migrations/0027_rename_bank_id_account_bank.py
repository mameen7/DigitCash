# Generated by Django 3.2.13 on 2022-06-06 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0026_auto_20220605_1313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='bank_id',
            new_name='bank',
        ),
    ]