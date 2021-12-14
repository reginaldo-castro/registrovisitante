from django.shortcuts import render
from visitantes.models import Visitante
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required
def index(request):

    todos_visitantes = Visitante.objects.order_by("-horario_chegada")

    visitante_aguardando = todos_visitantes.filter(
        status = "AGUARDANDO"
    )

    visitante_em_visitas = todos_visitantes.filter(
        status = "EM_VISITA"
    )

    visitante_finalizado = todos_visitantes.filter(
        status = "FINALIZADO"
    )

    hora_atual = timezone.now()
    mes_atual = hora_atual.month

    visitante_mes = todos_visitantes.filter(
        horario_chegada__month = mes_atual
    )


    context = {
        "nome_pagina": "Início da dashboard",
        "todos_visitantes": todos_visitantes,
        "visitante_aguardando": visitante_aguardando.count(),
        "visitante_em_visitas": visitante_em_visitas.count(),
        "visitante_finalizado": visitante_finalizado.count(),
        "visitante_mes": visitante_mes.count(),
    }

    return render(request, 'index.html', context)