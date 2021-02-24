# Generated by Django 2.1 on 2018-09-21 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0005_auto_20180921_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='costo',
            field=models.DecimalField(decimal_places=5, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='foto',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='huella',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='latitud',
            field=models.DecimalField(decimal_places=10, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='longitud',
            field=models.DecimalField(decimal_places=5, max_digits=15, null=True),
        ),
    ]