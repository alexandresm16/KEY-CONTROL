from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html', extra_context={'titulo': 'Autenticação'}), name='login'),
    path('sair/', auth_views.LogoutView.as_view(), name="logout"),
    path('alterar_sanha/', auth_views.PasswordChangeView.as_view(template_name='login.html', extra_context={'titulo': 'Alterar Senha'},
                                               success_url=reverse_lazy('index')), name="alterar_senha"),
]
