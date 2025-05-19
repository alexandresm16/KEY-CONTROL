from django import forms

from chavebloco.models import ChaveBloco


class ChaveBlocoModelForm(forms.ModelForm):
    class Meta:
        model = ChaveBloco
        fields = ['bloco', 'codigo']
        widgets = {
            'codigo': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o código da Chave'}),
        }

        error_messages = {
            'codigo': {'required': 'O codigo da chave é um campo obrigatório',
                       'unique': 'Código da chave já cadastrado'},
        }
