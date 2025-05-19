from django.db import models
from django.db.models.functions import Upper


# Create your models here.

class ChaveBloco(models.Model):

    DISPONIBILIDADE_CHAVE = [
        ('S', 'sim'),
        ('N', 'não'),
    ]

    bloco = models.ForeignKey('bloco.Bloco', verbose_name='Bloco', on_delete=models.PROTECT,
                              related_name='bloco', help_text='Bloco da chave')
    codigo = models.CharField('Código', max_length=10, help_text='Código da chave do bloco', unique=True)

    disponibilidade = models.CharField('Disponibilidade', max_length=1, help_text='Disponibilidade da chave',
                                       choices=DISPONIBILIDADE_CHAVE, default='S')

    class Meta:
        verbose_name = 'Chave do Bloco'
        verbose_name_plural = 'Chaves do Bloco'
        ordering = [Upper('bloco__nome'),]

    def __str__(self):
        return f'Chave: {self.codigo} - Bloco: ({self.bloco})'
