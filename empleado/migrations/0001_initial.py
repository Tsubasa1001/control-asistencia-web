# Generated by Django 2.1 on 2018-09-13 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('punto', models.CharField(max_length=200)),
                ('coordenada', models.DecimalField(decimal_places=10, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('detalle', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ci', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('latitud', models.DecimalField(decimal_places=10, max_digits=15)),
                ('longitud', models.DecimalField(decimal_places=5, max_digits=15)),
                ('foto', models.ImageField(upload_to='')),
                ('huella', models.ImageField(upload_to='')),
                ('telefono', models.CharField(max_length=20)),
                ('costo', models.DecimalField(decimal_places=5, max_digits=5)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleado.Cargo')),
            ],
        ),
        migrations.CreateModel(
            name='EstadoEmpleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('detalle', models.CharField(max_length=200)),
                ('color', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.CharField(max_length=200)),
                ('coordenada', models.DecimalField(decimal_places=10, max_digits=15)),
                ('nombre', models.CharField(max_length=200)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleado.Area')),
            ],
        ),
        migrations.AddField(
            model_name='empleado',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleado.EstadoEmpleado'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='zona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleado.Zona'),
        ),
    ]
