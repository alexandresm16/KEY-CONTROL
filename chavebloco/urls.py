from django.urls import path
from chavebloco.views import ChaveBlocoView, ChaveBlocoAddView, ChaveBlocoDeleteView, ChaveBlocoUpDateView

urlpatterns = [
    path('chavebloco', ChaveBlocoView.as_view(), name='chave_bloco'),
    path('chavebloco/adicionar', ChaveBlocoAddView.as_view(), name='cadastro_chave_bloco'),
    path('<int:pk>/chavebloco/editar', ChaveBlocoUpDateView.as_view(), name='editar_chave_bloco'),
    path('<int:pk>/chavebloco/apagar', ChaveBlocoDeleteView.as_view(), name='apagar_chave_bloco'),
]