# Generated by Django 3.2.9 on 2021-11-14 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_otplog_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='trx_pin',
            field=models.CharField(blank=True, max_length=6, null=True, unique=True),
        ),
    ]
