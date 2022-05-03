from django.db import models

# Create your models here.
class Acompaniante (models.Model):
    name = models.CharField(max_length=50)
    age = models.FloatField(null=True, blank=True, default=None)
    email = models.CharField(max_length=50)
    sueldo = models.CharField(max_length=50)


    def __str__(self):
        return '{}'.format(self.name)