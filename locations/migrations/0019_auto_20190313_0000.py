# Generated by Django 2.1.7 on 2019-03-13 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0018_auto_20190312_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='phone1',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Phone #1'),
        ),
        migrations.AlterField(
            model_name='location',
            name='phone2',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Phone #2'),
        ),
    ]
