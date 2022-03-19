from datetime import datetime
from time import strftime
from ..models import Estudiante
from ..models import Semestre

def get_semestres():
    semestres = Semestre.objects.all()
    return semestres

def get_semestre(mea_pk):
    semestre = Semestre.objects.get(pk=mea_pk)
    return semestre

def update_semestre(mea_pk, new_mea):
    semestre = get_semestre(mea_pk)
    semestre.estudiante = Estudiante.objects.get(pk=new_mea["estudiante"])
    semestre.valor = new_mea["valor"]
    semestre.periodo = new_mea["periodo"]
    semestre.save()
    return semestre

def create_semestre(mea):
    semestre = Semestre(estudiante=Estudiante.objects.get(pk=mea["estudiante"]), valor=mea["valor"], periodo=mea["periodo"])
    semestre.save()
    return semestre

def delete_semestre(mea_pk):
    semestre = get_semestre(mea_pk)
    semestre.delete()
    return semestre