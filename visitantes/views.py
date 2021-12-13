from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from visitantes.forms import visitanteForm
from visitantes.models import Visitante

def registrar_visitante(request):
    form = visitanteForm

    if request.method == "POST":
        form = visitanteForm(request.POST)
       
        if form.is_valid():
            visitante = form.save(commit=False)

            visitante.registrado_por = request.user.porteiro
        
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


    context = {
        "nome_pagina": "Informações do visitante",
        "visitante": visitante
    }
    return render(request, 'informacoes_visitante.html', context)


