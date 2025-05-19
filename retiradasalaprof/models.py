from django.db import models
from django.utils.timezone import now
from django.db.models.functions import Upper


# Create your models here.

class RetiradaSalaProf(models.Model):
    situacao = (
        ("Retirada", "Retirada"),
        ("Devolvida", "Devolvida"),
        ("Expirada", "Expirada")
    )

    professor = models.ForeignKey('professor.Professor', verbose_name='Professor', on_delete=models.PROTECT,
                                    related_name='professor_sala', help_text='Professor Retirante')
    chave = models.ForeignKey('chavesala.ChaveSala', verbose_name='Chave Sala', on_delete=models.PROTECT,
                              related_name='retirada_chavesalap', help_text='Chave retirada', limit_choices_to={'disponibilidade': 'S'})
    data = models.DateTimeField('Data', default=now, editable=True, help_text='Data de retirada')
    devolucao = models.DateTimeField('Devolução', default=now, editable=True, help_text='Data de devolução')
    status = models.CharField('Status', max_length=9, help_text='Status da Retirada', default='Retirada')

    class Meta:
        verbose_name = 'Retirada de Sala Prof'
        verbose_name_plural = 'Retiradas de Salas Profs'
        ordering = ['-devolucao', ]

    def __str__(self):
        return f'{self.chave}'
