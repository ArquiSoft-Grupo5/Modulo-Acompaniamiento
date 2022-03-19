from ..models import Estudiante

def get_estudiantes():
    estudiantes = Estudiante.objects.all()
    return estudiantes

def get_estudiante(var_pk):
    estudiante = Estudiante.objects.get(pk=var_pk)
    return estudiante

def update_estudiante(var_pk, new_var):
    estudiante = get_estudiante(var_pk)
    estudiante.name = new_var["name"]
    estudiante.save()
    return estudiante

def create_estudiante(var):
    estudiante = Estudiante(name=var["name"])
    estudiante.save()
    return estudiante