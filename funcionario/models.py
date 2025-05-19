from django.db import models
from django.db.models.functions import Upper

from home.models import Pessoa

# Create your models here.

class Funcionario(Pessoa):
    funcao = models.CharField('Função', max_length=35, help_text='Função desenvolvida pelo funcionario')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
        ordering = [Upper('nome'),]

    def __str__(self):
        return super().nome