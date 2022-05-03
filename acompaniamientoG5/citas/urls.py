from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import include

from . import views

urlpatterns = [
    path('citas/', views.cita_list, name='citaList'),
    path('cita/<id>', views.single_cita, name='singleCita'),
    path('citacreate/', csrf_exempt(views.cita_create), name='citaCreate'),
]