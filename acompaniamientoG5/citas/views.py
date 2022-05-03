from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import CitaForm
from .logic.citas_logic import get_citas, get_cita, create_cita
from django.contrib.auth.decorators import login_required
#from acompaniamientoG5.auth0backend import getRole

@login_required
def cita_list(request):
    citas = get_citas()
    context = {
        'cita_list': citas
    }
    return render(request, 'Cita/citas.html', context)

@login_required
def single_cita(request, id=0):
    cita = get_cita(id)
    context = {
        'cita': cita
    }
    return render(request, 'Cita/cita.html', context)

@login_required
def cita_create(request):
    role = "Acompaniante"#getRole(request)
    if role == "Acompaniante":
        if request.method == 'POST':
            form = CitaForm(request.POST)
            if form.is_valid():
                create_cita(form)
                messages.add_message(request, messages.SUCCESS, 'Successfully created cita')
                return HttpResponseRedirect(reverse('citaCreate'))
            else:
                print(form.errors)
        else:
            form = CitaForm()

        context = {
            'form': form,
        }
        return render(request, 'Cita/citaCreate.html', context)
    else:
        return HttpResponse("Unauthorized User")