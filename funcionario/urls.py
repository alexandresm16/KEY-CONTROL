from django.urls import path
from .views import FuncionariosView, FuncionarioAddView, FuncionarioUpDateView, FuncionarioDeleteView

urlpatterns = [
    path('funcionarios', FuncionariosView.as_view(), name='funcionarios'),
    path('funcionario/adicionar', FuncionarioAddView.as_view(), name='cadastro_funcionario'),
    path('<int:pk>/funcionario/editar/', FuncionarioUpDateView.as_view(), name='editar_funcionario'),
    path('<int:pk>/funcionario/apagar/', FuncionarioDeleteView.as_view(), name='apagar_funcionario'),
]