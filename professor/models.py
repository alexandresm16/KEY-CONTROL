from django.db import models
from django.db.models.functions import Upper

from home.models import Pessoa


# Create your models here.

class Professor(Pessoa):
    matricula = models.CharField('Matricula', max_length=12, help_text='Matricula UFSM')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = [Upper('nome'),]



    def __str__(self):
        return super().nome