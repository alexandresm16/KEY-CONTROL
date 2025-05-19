from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from retiradasalafunc.forms import RetiradaSalaFuncModelForm
from retiradasalafunc.models import RetiradaSalaFunc


# Create your views here.

class RetiradaSalaFuncView(ListView):
    model = RetiradaSalaFunc
    template_name = 'retirada_sala.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(RetiradaSalaFuncView, self).get_queryset()
        for retirada in qs:
            if retirada.status == 'Retirada':
                chave = retirada.chave
                chave.disponibilidade = 'N'
                chave.save()
                if retirada.devolucao < timezone.now():
                    retirada.status = 'Expirada'
                    retirada.chave.disponibilidade = 'N'
                    retirada.save()
        if buscar:
            qs = qs.filter(chave__codigo__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 10)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, "Não existem chaves cadastradas!")


class RetiradaSalaFuncAddView(SuccessMessageMixin, CreateView):
    form_class = RetiradaSalaFuncModelForm
    model = RetiradaSalaFunc
    template_name = 'retirada_chave_bloco.html'
    success_url = reverse_lazy('retirada_sala')
    success_message = 'Retirada da Chave realizada com sucesso!'


class RetiradaSalaFuncUpDateView(SuccessMessageMixin, UpdateView):
    form_class = RetiradaSalaFuncModelForm
    model = RetiradaSalaFunc
    template_name = 'retirada_chave_sala.html'
    success_url = reverse_lazy('retirada_sala')
    success_message = 'Retirada da Chave alterada com sucesso!'


class RetiradaSalaFuncDeleteView(SuccessMessageMixin, DeleteView):
    model = RetiradaSalaFunc
    template_name = 'apagar_retirada_sala.html'
    success_url = reverse_lazy('retirada_sala')
    success_message = 'Retirada da chave de sala excluida com sucesso!'


class RetiradaSalaFuncDetailView(SuccessMessageMixin, DetailView):
    model = RetiradaSalaFunc
    template_name = 'detail_retirada_sala.html'
    success_url = reverse_lazy('retirada_sala')
    success_message = 'Chave devolvida com sucesso!'

    def get_object(self, queryset=None):
        retirada = RetiradaSalaFunc.objects.get(pk=self.kwargs.get('pk'))
        retirada.status = 'Devolvida'
        chave = retirada.chave
        chave.disponibilidade = 'S'
        chave.save()
        retirada.save()
        return retirada
