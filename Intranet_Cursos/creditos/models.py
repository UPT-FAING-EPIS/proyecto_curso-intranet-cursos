from django.db import models

# Create your models here.
class Creditos(models.Model):
    CodCredito = models.AutoField(primary_key=True)
    TipCredito= models.CharField(max_length=50)
    