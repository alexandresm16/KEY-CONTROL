from django import forms

from .models import Sala


class SalaModelForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['bloco', 'andar', 'numero', 'uso']
        widgets = {
            'numero': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite a identificação da Sala'}),
        }

        error_messages = {
            'numero': {'required': 'A identificação da Sala é um campo obrigatório',
                       'unique': 'Identificação da Sala já cadastrada'},
            'bloco': {'required': 'O Bloco da Sala é um campo obrigatório'},
            'andar': {'required': 'O Andar da Sala é um campo obrigatório'},
            'uso': {'required': 'O Uso da Sala é um campo obrigatório'},
        }
