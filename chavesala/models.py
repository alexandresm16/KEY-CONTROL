from django.db import models
from django.db.models.functions import Upper


# Create your models here.

class ChaveSala(models.Model):

    DISPONIBILIDADE_CHAVE = [
        ('S', 'sim'),
        ('N', 'não'),
    ]

    sala = models.ForeignKey('sala.Sala', verbose_name='Sala', on_delete=models.PROTECT,
                             related_name='sala_chave', help_text='Sala da chave')
    codigo = models.CharField('Código', max_length=10, help_text='Código da chave da Sala', unique=True)
    disponibilidade = models.CharField('Disponibilidade', max_length=1, help_text='Disponibilidade da chave',
                                       choices=DISPONIBILIDADE_CHAVE, default='S')

    class Meta:
        verbose_name = 'Chave da Sala'
        verbose_name_plural = 'Chaves das Salas'
        ordering = [Upper('sala__numero'), ]

    def __str__(self):
        return f'Chave: {self.codigo} - ({self.sala})'
