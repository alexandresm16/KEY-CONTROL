from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.functions import Upper


class Bloco(models.Model):
    nome = models.CharField('Nome', max_length=10, help_text='Nome ou código do bloco', unique=True)
    andares = models.DecimalField('Andares', max_digits=1, decimal_places=0, help_text='Número de andares do bloco', default=1,
                                  validators=[MinValueValidator(1),
                                              MaxValueValidator(3)]
                                  )

    class Meta:
        verbose_name = 'Bloco'
        verbose_name_plural = 'Blocos'
        ordering = [Upper('nome'),]

    def __str__(self):
        return self.nome


