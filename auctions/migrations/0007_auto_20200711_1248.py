# Generated by Django 3.0.8 on 2020-07-11 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20200711_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='description',
            field=models.TextField(max_length=65),
        ),
        migrations.AlterField(
            model_name='items',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
