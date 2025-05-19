from django.urls import path
from .views import SalasView, SalasAddView, SalasUpDateView, SalasDeleteView

urlpatterns = [
    path('salas', SalasView.as_view(), name='salas'),
    path('salas/adicionar', SalasAddView.as_view(), name='cadastro_sala'),
    path('<int:pk>/salas/editar', SalasUpDateView.as_view(), name='editar_sala'),
    path('<int:pk>/salas/excluir', SalasDeleteView.as_view(), name='excluir_sala'),
]