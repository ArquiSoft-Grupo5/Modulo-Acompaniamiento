from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.preAnalisis_view, name='preAnalisis_view'),
    path('<int:pk>', views.preAnalisis_view, name='preAnalisis_view'),
]