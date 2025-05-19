from django.urls import path

from retiradasalafunc.views import RetiradaSalaFuncView, RetiradaSalaFuncAddView, RetiradaSalaFuncUpDateView, \
    RetiradaSalaFuncDeleteView, RetiradaSalaFuncDetailView

urlpatterns = [
    path('retiradasala', RetiradaSalaFuncView.as_view(), name='retirada_sala'),
    path('retiradasala/adicionar', RetiradaSalaFuncAddView.as_view(), name='retirada_chave_sala'),
    path('<int:pk>/retiradasala/editar', RetiradaSalaFuncUpDateView.as_view(), name='editar_retirada_sala'),
    path('<int:pk>/retiradasala/apagar', RetiradaSalaFuncDeleteView.as_view(), name='apagar_retirada_sala'),
    path('<int:pk>/retiradasala/detail', RetiradaSalaFuncDetailView.as_view(), name='detail_retirada_sala'),
]