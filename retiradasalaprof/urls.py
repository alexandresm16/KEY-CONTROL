from django.urls import path
from retiradasalaprof.views import (RetiradaSalaProfView, RetiradaSalaProfAddView, RetiradaSalaProfUpDateView,
                                    RetiradaSalaProfDeleteView, RetiradaSalaProfDetailView)

urlpatterns = [
    path('retiradasalap', RetiradaSalaProfView.as_view(), name='retirada_salap'),
    path('retiradasalap/adicionar', RetiradaSalaProfAddView.as_view(), name='retirada_chave_salap'),
    path('<int:pk>/retiradasalap/editar', RetiradaSalaProfUpDateView.as_view(), name='editar_retirada_salap'),
    path('<int:pk>/retiradasalap/apagar', RetiradaSalaProfDeleteView.as_view(), name='apagar_retirada_salap'),
    path('<int:pk>/retiradasalap/detail', RetiradaSalaProfDetailView.as_view(), name='detail_retirada_salap'),
]