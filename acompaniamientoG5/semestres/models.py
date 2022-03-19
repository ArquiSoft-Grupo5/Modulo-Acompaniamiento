from django.db import models

# Create your models here.

from estudiantes.models import Estudiante

class Semestre(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, default=None)
    valor = models.FloatField(null=True, blank=True, default=None)
    periodo = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' % (self.valor, self.periodo)