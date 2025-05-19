from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from retiradablocop.forms import RetiradaBlocoPModelForm
from retiradablocop.models import RetiradaBlocoP

from django.utils.timezone import now


# Create your views here.
class RetiradaBlocoPView(ListView):
    model = RetiradaBlocoP
    template_name = 'retirada_blocop.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(RetiradaBlocoPView, self).get_queryset()
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


class RetiradaBlocoPAddView(SuccessMessageMixin, CreateView):
    form_class = RetiradaBlocoPModelForm
    model = RetiradaBlocoP
    template_name = 'retirada_chave_blocop.html'
    success_url = reverse_lazy('retirada_blocop')
    success_message = 'Retirda da Chave realizada com sucesso!'


class RetiradaBlocoPUpDateView(SuccessMessageMixin, UpdateView):
    form_class = RetiradaBlocoPModelForm
    model = RetiradaBlocoP
    template_name = 'retirada_chave_blocop.html'
    success_url = reverse_lazy('retirada_blocop')
    success_message = 'Retirda da Chave alterada com sucesso!'


class RetiradaBlocoPDeleteView(SuccessMessageMixin, DeleteView):
    model = RetiradaBlocoP
    template_name = 'apagar_retirada_blocop.html'
    success_url = reverse_lazy('retirada_blocop')
    success_message = 'Retirada da chave do bloco excluida com sucesso!'


class RetiradaBlocoPDetailView(SuccessMessageMixin, DetailView):
    model = RetiradaBlocoP
    template_name = 'detail_retirada_blocop.html'
    success_url = reverse_lazy('retirada_blocop')
    success_message = 'Chave devolvida com sucesso!'

    def get_object(self, queryset=None):
        retirada = RetiradaBlocoP.objects.get(pk=self.kwargs.get('pk'))
        retirada.status = 'Devolvida'
        chave = retirada.chave
        chave.disponibilidade = 'S'
        chave.save()
        retirada.save()
        retirada.save()
        return retirada
