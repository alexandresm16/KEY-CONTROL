from django import forms

from .models import Funcionario


class FuncionarioModelForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'funcao', 'fone', 'email']
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o nome do funcionário'}),
            'funcao': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite a função do funcionáro'}),
            'fone': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite número de telefone'}),
            'email': forms.EmailInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o e-mail do funcionário'}),
        }
    error_messages = {
        'nome': {'required': 'O nome do funcionario é um campo obrigatório'},
        'funcao': {'required': 'A funcao do funcionario é um campo obrigatório'},
        'fone': {'required': 'O número do telefone do funcionario é um campo obrigatório'},
        'email': {'required': 'O e-mail do funcionario é um campo obrigatório,',
                  'invalid': 'Formato inválido para o e-mail. Exemplo de formato válido: fulano@dominio.com',
                  'unique': 'E-mail já cadastrado'},
    }
