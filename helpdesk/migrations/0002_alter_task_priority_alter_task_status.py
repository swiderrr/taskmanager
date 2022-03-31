# Generated by Django 4.0.3 on 2022-03-28 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('1', 'Niski'), ('2', 'Normalny'), ('3', 'Wysoki')], default='Niski', max_length=10, null='false'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('1', 'Stworzono'), ('2', 'W trakcie'), ('3', 'Częściowo rozwiązany'), ('4', 'Rozwiązany'), ('5', 'Zamknięty')], default='Stworzono', max_length=30, null='false'),
        ),
    ]