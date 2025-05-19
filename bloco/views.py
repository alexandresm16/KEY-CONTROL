from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models.deletion import ProtectedError
from django.shortcuts import get_object_or_404, render

from bloco.forms import BlocoModelForm
from bloco.models import Bloco


class BlocosView(ListView):
    model = Bloco
    template_name = "blocos.html"

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(BlocosView, self).get_queryset()
        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 10)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, "Não existem blocos cadastrados!")


class BlocosAddView(SuccessMessageMixin, CreateView):
    form_class = BlocoModelForm
    model = Bloco
    template_name = 'cadastro_bloco.html'
    success_url = reverse_lazy('blocos')
    success_message = 'Bloco cadastrado com sucesso!'


class BlocosUpDateView(SuccessMessageMixin, UpdateView):
    form_class = BlocoModelForm
    model = Bloco
    template_name = 'cadastro_bloco.html'
    success_url = reverse_lazy('blocos')
    success_message = 'Bloco alterado com sucesso!'


class BlocosDeleteView(SuccessMessageMixin, DeleteView):
    model = Bloco
    template_name = 'excluir_bloco.html'
    success_url = reverse_lazy('blocos')
    success_message = 'Bloco excluido com sucesso!'

