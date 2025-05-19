from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from professor.forms import ProfessorModelForm
from professor.models import Professor


# Create your views here.

class ProfessoresView(ListView):
    permission_required = 'professor.view_professor'
    permission_denied_message = 'Visualizar professor'
    model = Professor
    template_name = 'professores.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(ProfessoresView, self).get_queryset()
        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 10)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, "Não existem professores cadastrados!")


class ProfessoresAddView(SuccessMessageMixin, CreateView):
    form_class = ProfessorModelForm
    model = Professor
    template_name = 'cadastro_professor.html'
    success_url = reverse_lazy('professores')
    success_message = 'Professor cadastrado com sucesso!'


class ProfessoresUpDateView(SuccessMessageMixin, UpdateView):
    form_class = ProfessorModelForm
    model = Professor
    template_name = 'cadastro_professor.html'
    success_url = reverse_lazy('professores')
    success_message = 'Professor alterado com sucesso!'


class ProfessoresDeleteView(SuccessMessageMixin, DeleteView):
    model = Professor
    template_name = 'apagar_professor.html'
    success_url = reverse_lazy('professores')
    success_message = 'Professor apagado com sucesso!'