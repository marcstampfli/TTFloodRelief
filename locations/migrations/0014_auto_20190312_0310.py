# Generated by Django 2.1.7 on 2019-03-12 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0013_auto_20190312_0309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='phone2',
            field=models.IntegerField(blank=True, null=True, verbose_name='Phone #2'),
        ),
    ]