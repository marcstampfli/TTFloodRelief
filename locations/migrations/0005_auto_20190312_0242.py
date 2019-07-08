# Generated by Django 2.1.7 on 2019-03-12 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0004_auto_20190310_0139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='google_map',
        ),
        migrations.AlterField(
            model_name='location',
            name='address1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='location',
            name='address2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='location',
            name='cardinal_point',
            field=models.CharField(choices=[('North', 'North'), ('East', 'East'), ('South', 'South'), ('West', 'West')], default='None', max_length=1),
        ),
        migrations.AlterField(
            model_name='location',
            name='close_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='contact1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='location',
            name='contact2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='location',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='email',
            field=models.EmailField(max_length=255),
        ),
        migrations.AlterField(
            model_name='location',
            name='facebook',
            field=models.URLField(max_length=255),
        ),
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='location',
            name='notes',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='open_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='phone1',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='phone2',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='town',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='location',
            name='website',
            field=models.URLField(max_length=255),
        ),
    ]