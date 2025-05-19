from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from funcionario.forms import FuncionarioModelForm
from funcionario.models import Funcionario


# Create your views here.


class FuncionariosView(ListView):
    model = Funcionario
    template_name = 'funcionarios.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(FuncionariosView, self).get_queryset()
        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 10)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, "Não existem funcionários cadastrados!")


class FuncionarioAddView(SuccessMessageMixin, CreateView):
    form_class = FuncionarioModelForm
    model = Funcionario
    template_name = 'cadastro_funcionario.html'
    success_url = reverse_lazy('funcionarios')
    success_message = 'Funcionário cadastrado com sucesso!'


class FuncionarioUpDateView(SuccessMessageMixin, UpdateView):
    form_class = FuncionarioModelForm
    model = Funcionario
    template_name = 'cadastro_funcionario.html'
    success_url = reverse_lazy('funcionarios')
    success_message = 'Funcionário alterado com sucesso!'


class FuncionarioDeleteView(SuccessMessageMixin, DeleteView):
    model = Funcionario
    template_name = 'apagar_funcionario.html'
    success_url = reverse_lazy('funcionarios')
    success_message = 'Funcionário excluido com sucesso!'
