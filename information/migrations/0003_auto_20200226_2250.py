# Generated by Django 3.0.3 on 2020-02-26 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0002_homepage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='description',
            new_name='descriptions',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='youtube',
            new_name='youtubelink',
        ),
    ]
