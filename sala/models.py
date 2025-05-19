from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.functions import Upper


class Sala(models.Model):

    tipos = (
        ("Exclusivo", "Exclusivo"),
        ("Comunitário", "Comunitário")
    )

    bloco = models.ForeignKey('bloco.Bloco', verbose_name='Bloco', on_delete=models.PROTECT,
                              related_name='sala_bloco', help_text='Bloco da Sala ou laboratório')
    andar = models.DecimalField('Andar', max_digits=1, decimal_places=0,
                                help_text='Número do andar da Sala ou laboratório',
                                default=1,
                                validators=[MinValueValidator(1),
                                            MaxValueValidator(3)]
                                )
    numero = models.CharField('numero', max_length=6, help_text='Identificação da sala ou laboratório', unique=True)
    uso = models.CharField('uso', max_length=11, choices=tipos, help_text='Tipo de uso da Sala ou laboratório',
                           blank=False, null=False)

    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'
        ordering = [Upper('bloco__nome'),]

    def __str__(self):
        return f'Sala: {self.numero} - Bloco: ({self.bloco})'
