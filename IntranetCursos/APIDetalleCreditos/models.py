from django.db import models

# Create your models here.
class TbCreditos(models.Model):
    CodCredito = models.AutoField(primary_key=True)
    cantidad= models.CharField(max_length=50)
    class Meta:
        db_table = 'TbDetalleCredito'
    