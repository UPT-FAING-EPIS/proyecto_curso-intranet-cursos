# Generated by Django 4.2 on 2023-04-24 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APIProfesor', '0003_rename_apedocente_tbprofesor_apellidodocente_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbprofesor',
            old_name='ApellidoDocente',
            new_name='ApellidoProfesor',
        ),
        migrations.RenameField(
            model_name='tbprofesor',
            old_name='CodigoDocente',
            new_name='CodigoProfesor',
        ),
        migrations.RenameField(
            model_name='tbprofesor',
            old_name='DireccionDocente',
            new_name='DireccionProfesor',
        ),
        migrations.RenameField(
            model_name='tbprofesor',
            old_name='EmailDocente',
            new_name='EmailProfesor',
        ),
        migrations.RenameField(
            model_name='tbprofesor',
            old_name='NombreDocente',
            new_name='NombreProfesor',
        ),
        migrations.RenameField(
            model_name='tbprofesor',
            old_name='NumeroDocente',
            new_name='NumeroProfesor',
        ),
    ]
