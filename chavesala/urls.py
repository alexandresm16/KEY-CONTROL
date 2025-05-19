from django.urls import path
from chavesala.views import ChaveSalaView, ChaveSalaAddView, ChaveSalaUpDateView, ChaveSalaDeleteView
urlpatterns = [
    path('chavesala', ChaveSalaView.as_view(), name='chave_sala'),
    path('chavesala/adicionar', ChaveSalaAddView.as_view(), name='cadastro_chave_sala'),
    path('<int:pk>/chavesala/editar', ChaveSalaUpDateView.as_view(), name='editar_chave_sala'),
    path('<int:pk>/chavesala/apagar', ChaveSalaDeleteView.as_view(), name='apagar_chave_sala'),
]