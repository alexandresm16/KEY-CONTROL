from django import forms

from chavesala.models import ChaveSala


class ChaveSalaModelForm(forms.ModelForm):
    class Meta:
        model = ChaveSala
        fields = ['sala', 'codigo']
        widgets = {
            'codigo': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o código da Chave'}),
        }

        error_messages = {
            'codigo': {'required': 'O codigo da chave é um campo obrigatório',
                       'unique': 'Código da chave já cadastrado'},
            'sala': {'required': 'Selecione uma sala'},
        }

