# Generated by Django 2.1 on 2018-09-25 22:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0002_auto_20180924_1111'),
        ('material', '0001_initial'),
        ('empleado', '0007_remove_estadoempleado_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_inicio', models.DateTimeField(default=django.utils.timezone.now)),
                ('hora_fin', models.DateTimeField(default=django.utils.timezone.now)),
                ('fechaInicio', models.DateField(auto_now=True)),
                ('fechaFin', models.DateField(auto_now=True)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleado.Empleado')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.Material')),
            ],
        ),
        migrations.CreateModel(
            name='EstadoSolicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('detalle', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.DateTimeField(default=django.utils.timezone.now)),
                ('detalle', models.CharField(max_length=200)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente')),
                ('estado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='solicitud.EstadoSolicitud')),
            ],
        ),
        migrations.CreateModel(
            name='TipoSolicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('detalle', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='solicitud',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitud.TipoSolicitud'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='solicitud',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitud.Solicitud'),
        ),
    ]
