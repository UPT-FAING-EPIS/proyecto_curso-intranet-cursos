from django.db import models

# Create your models here.
class TbProfesor(models.Model):
    CodigoDocente = models.AutoField(primary_key=True)
    NombreDocente= models.CharField(max_length=50)
    ApellidoDocente= models.CharField(max_length=50)
    EmailDocente= models.CharField(max_length=50)
    NumeroDocente= models.PositiveIntegerField()
    DireccionDocente= models.CharField(max_length=50)
    class Meta:
        db_table = 'TbProfesor'