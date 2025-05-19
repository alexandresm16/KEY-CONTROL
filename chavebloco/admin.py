from django.contrib import admin

from .models import ChaveBloco

# Register your models here.

@admin.register(ChaveBloco)
class ChaveBlocoAdmin(admin.ModelAdmin):
    list_display = ('bloco', 'codigo')
    search_fields = ('codigo',)