# Generated by Django 2.1.7 on 2019-03-12 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0017_auto_20190312_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
