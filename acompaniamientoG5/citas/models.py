from django.db import models

# Create your models here.

from acompañantes.models import Acompaniante

class Cita(models.Model):
    acompaniante = models.ForeignKey(Acompaniante, on_delete=models.CASCADE, default=None)
    fecha = models.FloatField(null=True, blank=True, default=None)
    hora = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' % (self.fecha, self.hora)