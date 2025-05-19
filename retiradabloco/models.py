from django.db import models
from django.utils.timezone import now
from django.db.models.functions import Upper


# Create your models here.

class RetiradaBloco(models.Model):
    situacao = (
        ("Retirada", "Retirada"),
        ("Devolvida", "Devolvida"),
        ("Expirada", "Expirada")
    )

    funcionario = models.ForeignKey('funcionario.Funcionario', verbose_name='Funcionario', on_delete=models.PROTECT,
                                    related_name='funcionario_bloco', help_text='Funcionario Retirante')
    chave = models.ForeignKey('chavebloco.ChaveBloco', verbose_name='Chave Bloco', on_delete=models.PROTECT,
                              related_name='retirada_chavebloco', help_text='Chave retirada', limit_choices_to={'disponibilidade': 'S'})
    data = models.DateTimeField('Data', default=now, editable=True, help_text='Data de retirada')
    devolucao = models.DateTimeField('Devolução', default=now, editable=True, help_text='Data de devolução')
    status = models.CharField('Status', max_length=9, help_text='Status da Retirada', default='Retirada')

    class Meta:
        verbose_name = 'Retirada de Bloco'
        verbose_name_plural = 'Retiradas de Blocos'
        ordering = ['-devolucao', ]

    def __str__(self):
        return f'{self.chave}'

