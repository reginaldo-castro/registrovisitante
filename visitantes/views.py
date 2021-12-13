from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from visitantes.forms import visitanteForm, AutorizaVisitanteForm
from visitantes.models import Visitante
from django.utils import timezone

def registrar_visitante(request):
    form = visitanteForm

    if request.method == "POST":
        form = visitanteForm(request.POST)
        
        if form.is_valid():
            visitante = form.save(commit=False)
            
            visitante.registrado_por = request.user.porteiro    
            visitante.status == "EM_VISITA"
            visitante.horario_chegada = timezone.now()
            print(visitante)
            visitante.save()

            messages.success(
                request,
                "Visitante registrado com sucesso"
            )
            return redirect("index")

    context = {
        "nome_pagina":  "Registrar visitante",
        "form": form
    }

    return render(request, 'registrar_visitante.html', context)


def informacoes_visistantes(request, id):

    visitante = get_object_or_404(Visitante, id=id)
    
    form = AutorizaVisitanteForm()
    print(form)
    if request.method == "POST":
        form = AutorizaVisitanteForm(
            request.POST, instance=visitante
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Entrada do visitante autorizada com sucesso"
            )

    context = {
        "nome_pagina": "Informações do visitante",
        "visitante": visitante,
        "form": form
    }
    return render(request, 'informacoes_visitante.html', context)

