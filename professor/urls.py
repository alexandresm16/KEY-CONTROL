from django.urls import path
from .views import ProfessoresView, ProfessoresAddView, ProfessoresUpDateView, ProfessoresDeleteView

urlpatterns = [
    path('professores', ProfessoresView.as_view(), name='professores'),
    path('professores/adicionar/', ProfessoresAddView.as_view(), name='cadastro_professor'),
    path('<int:pk>/professores/editar/', ProfessoresUpDateView.as_view(), name='editar_professor'),
    path('<int:pk>/professores/apagar/', ProfessoresDeleteView.as_view(), name='apagar_professor'),
]