# Generated by Django 2.1 on 2018-09-21 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0006_auto_20180921_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estadoempleado',
            name='color',
        ),
    ]
