from django.db import models

# Create your models here.
class Visitante(models.Model):
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

    class Meta:
        verbose_name = "Visitante" 
        verbose_name_plural = "Visitantes"
        db_table = "visitante"
    
    def __str__(self):
        return self.nome_completo