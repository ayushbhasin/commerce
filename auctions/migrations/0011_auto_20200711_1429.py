# Generated by Django 3.0.8 on 2020-07-11 18:29

import auctions.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auto_20200711_1352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='startPrice',
            new_name='start_price',
        ),
        migrations.AlterField(
            model_name='items',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(auctions.models.Category), related_name='Items', to='auctions.Category'),
        ),
    ]
