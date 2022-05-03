from ..models import Acompaniante

def get_acompaniantes():
    acompaniantes = Acompaniante.objects.all()
    return acompaniantes

def get_acompaniante(var_pk):
    acompaniante = Acompaniante.objects.get(pk=var_pk)
    return acompaniante

def update_acompaniante(var_pk, new_var):
    acompaniante = get_acompaniante(var_pk)
    acompaniante.name = new_var["name"]
    acompaniante.age = new_var["age"]
    acompaniante.email = new_var["email"]
    acompaniante.sueldo = new_var["sueldo"]
    acompaniante.save()
    return acompaniante

def create_acompaniante(var):
    acompaniante = Acompaniante(name=var["name"],age=var["age"], email=var["email"], sueldo=var["sueldo"])
    acompaniante.save()
    return acompaniante