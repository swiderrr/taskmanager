# Generated by Django 4.0.3 on 2022-04-06 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0011_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]