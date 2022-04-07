from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views
urlpatterns = [
    path('', views.semestres_view, name='semestres_view'),
    path('<int:pk>', views.semestre_view, name='semestre_view'),
    path('create/', csrf_exempt(views.semestres_view), name='create'),
]
