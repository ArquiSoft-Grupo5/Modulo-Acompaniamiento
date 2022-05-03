from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.acompaniantes_view, name='acompaniantes_view'),
    path('<int:pk>', views.acompaniante_view, name='acompaniante_view'),
]