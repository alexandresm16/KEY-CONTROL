from django.contrib import admin

from .models import Funcionario

# Register your models here.

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'funcao', 'fone', 'email')
    search_fields = ('nome', 'funcao', 'fone')
    list_filter = ('funcao', )