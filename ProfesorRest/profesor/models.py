from django.db import models

# Create your models here.
class Profesor(models.Model):
    CodDocente = models.AutoField(primary_key=True)
    NomDocente= models.CharField(max_length=50)
    ApeDocente= models.CharField(max_length=50)
    EmaDocente= models.CharField(max_length=50)
    NumDocente= models.PositiveIntegerField()
    DirDocente= models.CharField(max_length=50)
    