# Generated by Django 2.1.7 on 2019-03-12 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0009_auto_20190312_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='phone1',
            field=models.IntegerField(blank=True, verbose_name='Phone #1'),
        ),
        migrations.AlterField(
            model_name='location',
            name='phone2',
            field=models.IntegerField(blank=True, verbose_name='Phone #2'),
        ),
    ]
