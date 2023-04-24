from django.db import models
from APICursos.urls import TbEstado

# Create your models here.
class TbProfesor(models.Model):
    CodigoProfesor = models.AutoField(primary_key=True)
    NombreProfesor= models.CharField(max_length=50)
    ApellidoProfesor= models.CharField(max_length=50)
    EmailProfesor= models.CharField(max_length=50)
    NumeroProfesor= models.PositiveIntegerField()
    DireccionProfesor= models.CharField(max_length=50)
    TbEstado = models.ForeignKey(TbEstado, on_delete=models.CASCADE)

    class Meta:
        db_table = 'TbProfesor'