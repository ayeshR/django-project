# Generated by Django 3.0.3 on 2020-02-29 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0008_delete_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Information',
            new_name='LatestPost',
        ),
    ]