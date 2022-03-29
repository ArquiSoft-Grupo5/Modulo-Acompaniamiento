from .logic import semestres_logic as ml
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from .forms import SemestreForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

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
        form = SemestreForm(request.POST)
        if form.is_valid():
            ml.create_Semestre(form)
            messages.add_message(request, messages.SUCCESS, 'Semestre create successful')
            return HttpResponseRedirect(reverse('SemestreCreate'))
        else:
            print(form.errors)

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