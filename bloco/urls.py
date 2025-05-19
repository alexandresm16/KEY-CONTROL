from django.urls import path
from bloco.views import BlocosView, BlocosAddView, BlocosUpDateView, BlocosDeleteView

urlpatterns = [
    path('blocos', BlocosView.as_view(), name='blocos'),
    path('blocos/adicionar', BlocosAddView.as_view(), name='cadastro_bloco'),
    path('<int:pk>/blocos/editar', BlocosUpDateView.as_view(), name='editar_bloco'),
    path('<int:pk>/blocos/excluir', BlocosDeleteView.as_view(), name='excluir_bloco'),
]