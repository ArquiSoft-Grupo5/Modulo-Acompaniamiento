from .logic import acompañantes_logic as vl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def acompaniantes_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            acompaniante_dto = vl.get_acompaniante(id)
            acompaniante = serializers.serialize('json', [acompaniante_dto,])
            return HttpResponse(acompaniante, 'application/json')
        else:
            acompaniantes_dto = vl.get_acompaniantes()
            acompaniantes = serializers.serialize('json', acompaniantes_dto)
            return HttpResponse(acompaniantes, 'application/json')

    if request.method == 'POST':
        acompaniante_dto = vl.create_acompaniante(json.loads(request.body))
        acompaniante = serializers.serialize('json', [acompaniante_dto,])
        return HttpResponse(acompaniante, 'application/json')

@csrf_exempt
def acompaniante_view(request, pk):
    if request.method == 'GET':
        acompaniante_dto = vl.get_acompaniante(pk)
        acompaniante = serializers.serialize('json', [acompaniante_dto,])
        return HttpResponse(acompaniante, 'application/json')

    if request.method == 'PUT':
        acompaniante_dto = vl.update_acompaniante(pk, json.loads(request.body))
        acompaniante = serializers.serialize('json', [acompaniante_dto,])
        return HttpResponse(acompaniante, 'application/json')