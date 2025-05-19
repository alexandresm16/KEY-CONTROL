from django import forms
from retiradasalaprof.models import RetiradaSalaProf


class RetiradaSalaProfModelForm(forms.ModelForm):
    class Meta:
        model = RetiradaSalaProf
        fields = ['professor', 'chave', 'data', 'devolucao']

        error_messages = {
            'professor': {'required': 'Selecione um professor!'},
            'chave': {'required': 'Selecione um chave!'},
            'data': {'required': 'Informe a data atual!'},
            'devolucao': {'required': 'Informe a data de devolução!'},
        }

