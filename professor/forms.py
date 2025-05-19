from django import forms
from .models import Professor


class ProfessorModelForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'matricula', 'fone', 'email']
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o nome do Professor'}),
            'matricula': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite a matricula do Professor'}),
            'fone': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite telefone do Professor:'}),
            'email': forms.EmailInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o e-mail do Professor'}),
        }

        error_messages = {
            'nome': {'required': 'O nome do Profesor é um campo obrigatório',
                                 'unique': 'E-mail já cadastrado'},
            'matricula': {'required': 'A matricula do professor é um campo obrigatório'},
            'fone': {'required': 'O telefone do professor é um campo obrigatório'},
            'email': {'required': 'A email do professor é um campo obrigatório',
                      'invalid': 'Formato inválido para o e-mail. Exemplo de formato válido fulano@domino.com',
                      'unique': 'E-mail já cadastrado'},
        }