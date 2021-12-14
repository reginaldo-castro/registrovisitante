from django.db import models
from django.db.models.fields import DateField
from django.db.models.fields.related import OneToOneField

from usuarios.models import Usuario


# Create your models here.
class Porteiro(models.Model):
    usuario = OneToOneField("usuarios.Usuario", verbose_name="Usuário", on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=194, verbose_name="Nome completo")
    cpf = models.CharField(max_length=14, verbose_name="CPF")
    telefone = models.CharField(max_length=13, verbose_name="telefone de contato")
    data_nascimento = DateField(verbose_name="Data de nascimento", auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Porteiro"
        verbose_name_plural = "Porteiros"
        db_table = "porteiro"

    def __str__(self):
        return self.nome_completo