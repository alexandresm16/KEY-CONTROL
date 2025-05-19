from django import forms

from retiradabloco.models import RetiradaBloco


class RetiradaBlocoModelForm(forms.ModelForm):
    class Meta:
        model = RetiradaBloco
        fields = ['funcionario', 'chave', 'data', 'devolucao']

        error_messages = {
            'funcionario': {'required': 'Selecione um funcionario!'},
            'chave': {'required': 'Selecione um chave!'},
        }

