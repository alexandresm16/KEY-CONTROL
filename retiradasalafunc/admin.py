from django.contrib import admin
from .models import RetiradaSalaFunc


# Register your models here.
@admin.register(RetiradaSalaFunc)
class RetiradaSalaFuncAdmin(admin.ModelAdmin):
    list_display = ('funcionario', 'chave', 'data', 'devolucao')
    search_fields = ('funcionario', 'chave__codigo', 'data')
    list_filter = ('funcionario', 'status', 'chave__codigo')


