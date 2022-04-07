import time
from ..models import PreAnalisis

def get_preAnalisiss():
    time.sleep(0.5)
    preAnalisiss = PreAnalisis.objects.all()
    return preAnalisiss

def get_preAnalisis(var_pk):
    time.sleep(0.01)
    preAnalisis = PreAnalisis.objects.get(pk=var_pk)
    return preAnalisis

def update_preAnalisis(var_pk, new_var):
    preAnalisis = get_preAnalisis(var_pk)
    preAnalisis.name = new_var["name"]
    preAnalisis.save()
    return preAnalisis

def create_preAnalisis(var):
    preAnalisis = PreAnalisis(name=var["name"])
    preAnalisis.save()
    return preAnalisis
