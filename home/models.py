from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=50, help_text='Nome completo')
    fone = models.CharField('Telefone', max_length=14, help_text='Número de telefone - ex: (00)12345-6789', unique=True)
    email = models.EmailField('E-mail', max_length=100, help_text='Endereço de E-mail', unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome