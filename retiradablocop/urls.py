from django.urls import path
from retiradablocop.views import RetiradaBlocoPAddView, RetiradaBlocoPView, RetiradaBlocoPUpDateView, \
    RetiradaBlocoPDeleteView, RetiradaBlocoPDetailView

urlpatterns = [
    path('retiradablocop', RetiradaBlocoPView.as_view(), name='retirada_blocop'),
    path('retiradablocop/adicionar', RetiradaBlocoPAddView.as_view(), name='retirada_chave_blocop'),
    path('<int:pk>/retiradablocop/editar', RetiradaBlocoPUpDateView.as_view(), name='editar_retirada_blocop'),
    path('<int:pk>/retiradablocop/apagar', RetiradaBlocoPDeleteView.as_view(), name='apagar_retirada_blocop'),
    path('<int:pk>/retiradablocop/detail', RetiradaBlocoPDetailView.as_view(), name='detail_retirada_blocop'),
]