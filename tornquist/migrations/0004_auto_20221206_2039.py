# Generated by Django 3.2.14 on 2022-12-06 23:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tornquist', '0003_auto_20221128_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('ubicacion', models.CharField(blank=True, choices=[('', 'Seleccione una ubicacion'), ('Tornquist', 'Tornquist'), ('Sierra de la ventana', 'Sierra de la ventana')], max_length=200, null=True)),
                ('rubro', models.CharField(choices=[('', 'Seleccione un rubro'), ('Gastronomia', 'Gastronomia'), ('Actividades', 'Actividades'), ('Puntos de interes', 'Puntos de interes'), ('Alojamiento', 'Alojamiento')], max_length=20)),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('estado_respuesta', models.CharField(blank=True, choices=[('Aceptada', 'Aceptada'), ('Rechazada', 'Rechazada'), ('En revision', 'En revision')], default='En revision', max_length=15, null=True)),
                ('sitio', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono', models.CharField(blank=True, max_length=50, null=True)),
                ('url_img', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
                ('fecha', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name_plural': 'Solicitudes',
            },
        ),
        migrations.RemoveField(
            model_name='actividades',
            name='baja',
        ),
        migrations.RemoveField(
            model_name='gastronomia',
            name='baja',
        ),
        migrations.RemoveField(
            model_name='puntosinteres',
            name='baja',
        ),
        migrations.RemoveField(
            model_name='zonasalojamientos',
            name='baja',
        ),
        migrations.AddField(
            model_name='actividades',
            name='estado',
            field=models.CharField(choices=[('Aceptada', 'Aceptada'), ('Baja', 'Baja')], default='Aceptada', max_length=15),
        ),
        migrations.AddField(
            model_name='gastronomia',
            name='estado',
            field=models.CharField(choices=[('Aceptada', 'Aceptada'), ('Baja', 'Baja')], default='Aceptada', max_length=15),
        ),
        migrations.AddField(
            model_name='puntosinteres',
            name='estado',
            field=models.CharField(choices=[('Aceptada', 'Aceptada'), ('Baja', 'Baja')], default='Aceptada', max_length=15),
        ),
        migrations.AddField(
            model_name='zonasalojamientos',
            name='estado',
            field=models.CharField(choices=[('Aceptada', 'Aceptada'), ('Baja', 'Baja')], default='Aceptada', max_length=15),
        ),
        migrations.AlterField(
            model_name='actividades',
            name='url_img',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/Actividades/'),
        ),
        migrations.AlterField(
            model_name='gastronomia',
            name='url_img',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/Gastronomia/'),
        ),
        migrations.AlterField(
            model_name='puntosinteres',
            name='url_img',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/PuntosInteres/'),
        ),
        migrations.AlterField(
            model_name='zonasalojamientos',
            name='url_img',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/ZonasAlojamientos/'),
        ),
        migrations.CreateModel(
            name='RespuestaSolicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta', models.TextField()),
                ('estado_solicitud', models.CharField(blank=True, choices=[('Aceptada', 'Aceptada'), ('Rechazada', 'Rechazada'), ('En revision', 'En revision')], max_length=15, null=True)),
                ('fecha', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('solicitud', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tornquist.solicitud')),
            ],
        ),
    ]
