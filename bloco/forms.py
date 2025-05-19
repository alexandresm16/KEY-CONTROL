from django import forms

from .models import Bloco


class BlocoModelForm(forms.ModelForm):
    class Meta:
        model = Bloco
        fields = ['nome', 'andares']
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o código do Bloco'}),
        }

        error_messages = {
            'nome': {'required': 'O codigo do bloco é um campo obrigatório',
                     'unique': 'Código de bloco já cadastrado'},
            'andares': {'required': 'O numero de andres é um campo obrigatório'},
        }
