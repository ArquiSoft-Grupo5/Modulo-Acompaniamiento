from .logic import semestres_logic as ml
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def semestres_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            semestre_dto = ml.get_semestre(id)
            semestre = serializers.serialize('json', [semestre_dto,])
            return HttpResponse(semestre, 'application/json')
        else:
            semestres_dto = ml.get_semestres()
            semestres = serializers.serialize('json', semestres_dto)
            return HttpResponse(semestres, 'application/json')

    if request.method == 'POST':
        semestre_dto = ml.create_semestre(json.loads(request.body))
        semestre = serializers.serialize('json', [semestre_dto,])
        return HttpResponse(semestre, 'application/json')

@csrf_exempt
def semestre_view(request, pk):
    if request.method == 'GET':
        semestre_dto = ml.get_semestre(pk)
        semestre = serializers.serialize('json', [semestre_dto,])
        return HttpResponse(semestre, 'application/json')

    if request.method == 'PUT':
        semestre_dto = ml.update_semestre(pk, json.loads(request.body))
        semestre = serializers.serialize('json', [semestre_dto,])
        return HttpResponse(semestre, 'application/json')
    
    if request.method == 'DELETE':
        semestre_dto = ml.delete_semestre(pk)
        semestre = serializers.serialize('json', [semestre_dto,])
        return HttpResponse(semestre, 'application/json')