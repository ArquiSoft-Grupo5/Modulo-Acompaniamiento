from django.db import models
from estudiantes.models import Estudiante

# Create your models here.
class PreAnalisis(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, default=None)
    valor = models.FloatField(null=True, blank=True, default=None)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' % (self.estudiante, self.descripcion)