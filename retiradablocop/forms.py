from django import forms

from retiradablocop.models import RetiradaBlocoP


class RetiradaBlocoPModelForm(forms.ModelForm):
    class Meta:
        model = RetiradaBlocoP
        fields = ['professor', 'chave', 'data', 'devolucao']

        error_messages = {
            'professor': {'required': 'Selecione um professor!'},
            'chave': {'required': 'Selecione um chave!'},
        }


