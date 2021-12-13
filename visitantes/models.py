from django.db import models

# Create your models here.
class Visitante(models.Model):

    STATUS_VISITANTE = [
        ("AGUARDANDO", "Aguardando autorização"),
        ("EM_VISITA", "No setor"),
        ("FINALIZADO", "Visita finalizada"),
    ]

    nome_completo = models.CharField(verbose_name="Nome completo", max_length=194)
    cpf = models.CharField(verbose_name="CPF", max_length=11)
    data_nascimento = models.DateField(verbose_name="Data de nascimento", auto_now=False, auto_now_add=False)
    setor_visitado = models.CharField(verbose_name="setor a ser visitada", max_length=100)
    placa_veiculo = models.CharField(verbose_name="Placa do veículo", max_length=7, blank=True, null=True)
    horario_chegada = models.DateTimeField(verbose_name="Horário de chegada na portaria", auto_now_add=True)
    horario_saida = models.DateTimeField(verbose_name="Horário de saída da empresa", auto_now=False,blank=True, null=True)
    horario_autorizacao = models.DateTimeField(verbose_name="Horário de autorização de entrada", auto_now=False, blank=True, null=True)
    colaborador_responsavel = models.CharField(verbose_name="Nome do colaborador responsável por autorizar a entrada", max_length=194, blank=True)
    registrado_por = models.ForeignKey("porteiros.Porteiro", verbose_name="Porteiro responsável pelo registro", on_delete=models.PROTECT)
    status = models.CharField(verbose_name="Status", max_length=10, choices=STATUS_VISITANTE, default="AGUARDANDO",)

    def get_horario_saida(self):
        if self.horario_saida:
            return self.horario_saida
        return "Horário de saída não registrado"

    def get_horario_autorizacao(self):
        if self.horario_autorizacao:
            return self.horario_autorizacao
        return "Aguardando confirmação"

    def get_colaborador_responsavel(self):
        if self.colaborador_responsavel:
            return self.colaborador_responsavel
        return "Aguardando confirmação"

    def get_placa_veiculo(self):
        if self.placa_veiculo:
            return self.placa_veiculo
        return "Veículo não registrado"

    class Meta:
        verbose_name = "Visitante" 
        verbose_name_plural = "Visitantes"
        db_table = "visitante"
    
    def __str__(self):
        return self.nome_completo