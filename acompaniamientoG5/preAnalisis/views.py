from time import time
from .logic import preAnalisis_logic as vl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def preAnalisiss_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        time.sleep(1)
        if id:
            preAnalisis_dto = vl.get_preAnalisis(id)
            preAnalisis = serializers.serialize('json', [preAnalisis_dto, ])
            return HttpResponse(preAnalisis, 'application/json')
        else:
            preAnalisiss_dto = vl.get_preAnalisiss()
            preAnalisiss = serializers.serialize('json', preAnalisiss_dto)
            return HttpResponse(preAnalisiss, 'application/json')

    if request.method == 'POST':
        preAnalisis_dto = vl.create_preAnalisis(json.loads(request.body))
        preAnalisis = serializers.serialize('json', [preAnalisis_dto, ])
        return HttpResponse(preAnalisis, 'application/json')


@csrf_exempt
def preAnalisis_view(request, pk):
    if request.method == 'GET':
        time.sleep(1)
        preAnalisis_dto = vl.get_preAnalisis(pk)
        preAnalisis = serializers.serialize('json', [preAnalisis_dto, ])
        return HttpResponse(preAnalisis, 'application/json')

    if request.method == 'PUT':
        preAnalisis_dto = vl.update_preAnalisis(pk, json.loads(request.body))
        preAnalisis = serializers.serialize('json', [preAnalisis_dto, ])
        return HttpResponse(preAnalisis, 'application/json')
