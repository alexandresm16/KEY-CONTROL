from django.contrib import admin
from .models import RetiradaBlocoP


# Register your models here.
@admin.register(RetiradaBlocoP)
class RetiradaBlocoPAdmin(admin.ModelAdmin):
    list_display = ('professor', 'chave', 'data', 'devolucao')
    search_fields = ('professor', 'chave__codigo', 'data')
    list_filter = ('professor', 'status', 'chave__codigo')
