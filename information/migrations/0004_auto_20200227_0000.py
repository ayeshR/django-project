# Generated by Django 3.0.3 on 2020-02-26 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0003_auto_20200226_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='descriptions',
            field=models.CharField(max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='description',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
