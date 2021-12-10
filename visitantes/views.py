from django.shortcuts import render

from visitantes.forms import visitanteForm

def registrar_visitante(request):

    form = visitanteForm

    context = {
        "nome_pagina":  "Registrar visitante",
        "form": form
    }

    return render(request, 'registrar_visitante.html', context)
