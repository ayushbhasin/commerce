# Generated by Django 3.0.8 on 2020-07-11 00:07

import auctions.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20200710_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='category',
            field=models.ForeignKey(null=True, on_delete=models.SET(auctions.models.Category), to='auctions.Category'),
        ),
    ]
