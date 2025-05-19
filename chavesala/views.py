from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from chavesala.forms import ChaveSalaModelForm
from chavesala.models import ChaveSala


# Create your views here.


class ChaveSalaView(ListView):
    model = ChaveSala
    template_name = 'chave_sala.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(ChaveSalaView, self).get_queryset()

        if buscar:
            qs = qs.filter(
                Q(codigo__icontains=buscar) |   # Filtrar por código da chave
                Q(sala__numero__icontains=buscar) |  # Filtrar por número de sala
                Q(sala__bloco__nome__icontains=buscar)  # Filtrar por nome do bloco
            )

        if qs.count() > 0:
            paginator = Paginator(qs, 10)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, "Não existem chaves cadastradas!")


class ChaveSalaAddView(SuccessMessageMixin, CreateView):
    form_class = ChaveSalaModelForm
    model = ChaveSala
    template_name = 'cadastro_chave_sala.html'
    success_url = reverse_lazy('chave_sala')
    success_message = 'Chave de sala cadastrada com sucesso!'


class ChaveSalaUpDateView(SuccessMessageMixin, UpdateView):
    form_class = ChaveSalaModelForm
    model = ChaveSala
    template_name = 'cadastro_chave_sala.html'
    success_url = reverse_lazy('chave_sala')
    success_message = 'Chave de sala alterada com sucesso!'


class ChaveSalaDeleteView(SuccessMessageMixin, DeleteView):
    model = ChaveSala
    template_name = 'apagar_chave_sala.html'
    success_url = reverse_lazy('chave_sala')
    success_message = 'Chave de sala excluida com sucesso!'
