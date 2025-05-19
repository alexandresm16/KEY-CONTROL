from django import forms
from retiradasalafunc.models import RetiradaSalaFunc


class RetiradaSalaFuncModelForm(forms.ModelForm):
    class Meta:
        model = RetiradaSalaFunc
        fields = ['funcionario', 'chave', 'data', 'devolucao']

        error_messages = {
            'funcionario': {'required': 'Selecione um funcionario!'},
            'chave': {'required': 'Selecione um chave!'},
        }

