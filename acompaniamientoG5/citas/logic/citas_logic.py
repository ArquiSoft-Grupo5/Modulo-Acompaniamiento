from ..models import Cita

def get_citas():
    queryset = Cita.objects.all()
    return (queryset)

def get_cita(id):
    cita = Cita.objects.raw("SELECT * FROM citas_cita WHERE id=%s" % id)[0]
    return (cita)

def create_cita(form):
    cita = form.save()
    cita.save()
    return ()