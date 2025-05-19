from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateResponseMixin, View

from bloco.models import Bloco
from chavebloco.forms import ChaveBlocoModelForm
from chavebloco.models import ChaveBloco


# Create your views here.

class ChaveBlocoView(ListView):
    model = ChaveBloco
    template_name = 'chave_bloco.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(ChaveBlocoView, self).get_queryset()
        if buscar:
            qs = qs.filter(codigo__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 10)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, "Não existem chaves cadastradas!")


class ChaveBlocoAddView(SuccessMessageMixin, CreateView):
    form_class = ChaveBlocoModelForm
    model = ChaveBloco
    template_name = 'cadastro_chave_bloco.html'
    success_url = reverse_lazy('chave_bloco')
    success_message = 'Chave do bloco cadastrada com sucesso!'


class ChaveBlocoUpDateView(SuccessMessageMixin, UpdateView):
    form_class = ChaveBlocoModelForm
    model = ChaveBloco
    template_name = 'cadastro_chave_bloco.html'
    success_url = reverse_lazy('chave_bloco')
    success_message = 'Chave do bloco alterada com sucesso!'


class ChaveBlocoDeleteView(SuccessMessageMixin, DeleteView):
    model = ChaveBloco
    template_name = 'apagar_chave_bloco.html'
    success_url = reverse_lazy('chave_bloco')
    success_message = 'Chave do bloco excluida com sucesso!'
