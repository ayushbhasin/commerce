# Generated by Django 3.0.8 on 2020-07-11 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_auto_20200711_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='imageUrl',
            field=models.URLField(null=True),
        ),
    ]
