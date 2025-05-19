from django.urls import path
from retiradabloco.views import RetiradaBlocoAddView, RetiradaBlocoView, RetiradaBlocoUpDateView, \
    RetiradaBlocoDeleteView, RetiradaBlocoDetailView

urlpatterns = [
    path('retiradabloco', RetiradaBlocoView.as_view(), name='retirada_bloco'),
    path('retiradabloco/adicionar', RetiradaBlocoAddView.as_view(), name='retirada_chave_bloco'),
    path('<int:pk>/retiradabloco/editar', RetiradaBlocoUpDateView.as_view(), name='editar_retirada_bloco'),
    path('<int:pk>/retiradabloco/apagar', RetiradaBlocoDeleteView.as_view(), name='apagar_retirada_bloco'),
    path('<int:pk>/retiradabloco/detail', RetiradaBlocoDetailView.as_view(), name='detail_retirada_bloco'),
]
