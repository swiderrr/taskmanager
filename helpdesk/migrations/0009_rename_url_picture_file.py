# Generated by Django 4.0.3 on 2022-04-03 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0008_rename_picture_picture_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='picture',
            old_name='url',
            new_name='file',
        ),
    ]
