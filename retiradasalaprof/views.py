from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from retiradasalaprof.forms import RetiradaSalaProfModelForm
from retiradasalaprof.models import RetiradaSalaProf


# Create your views here.

class RetiradaSalaProfView(ListView):
    model = RetiradaSalaProf
    template_name = 'retirada_salap.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(RetiradaSalaProfView, self).get_queryset()
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


class RetiradaSalaProfAddView(SuccessMessageMixin, CreateView):
    form_class = RetiradaSalaProfModelForm
    model = RetiradaSalaProf
    template_name = 'retirada_chave_blocop.html'
    success_url = reverse_lazy('retirada_salap')
    success_message = 'Retirda da Chave realizada com sucesso!'


class RetiradaSalaProfUpDateView(SuccessMessageMixin, UpdateView):
    form_class = RetiradaSalaProfModelForm
    model = RetiradaSalaProf
    template_name = 'retirada_chave_salap.html'
    success_url = reverse_lazy('retirada_salap')
    success_message = 'Retirada da Chave alterada com sucesso!'


class RetiradaSalaProfDeleteView(SuccessMessageMixin, DeleteView):
    model = RetiradaSalaProf
    template_name = 'apagar_retirada_salap.html'
    success_url = reverse_lazy('retirada_salap')
    success_message = 'Retirada da chave de sala excluida com sucesso!'


class RetiradaSalaProfDetailView(SuccessMessageMixin, DetailView):
    model = RetiradaSalaProf
    template_name = 'detail_retirada_salap.html'
    success_url = reverse_lazy('retirada_salap')
    success_message = 'Chave devolvida com sucesso!'

    def get_object(self, queryset=None):
        retirada = RetiradaSalaProf.objects.get(pk=self.kwargs.get('pk'))
        retirada.status = 'Devolvida'
        chave = retirada.chave
        chave.disponibilidade = 'S'
        chave.save()
        retirada.save()
        return retirada
