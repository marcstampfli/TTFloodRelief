# Generated by Django 2.1.7 on 2019-03-12 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0007_auto_20190312_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='cardinal_point',
            field=models.CharField(choices=[('North', 'North'), ('East', 'East'), ('South', 'South'), ('West', 'West')], default='North', max_length=5),
        ),
    ]
