from django.contrib import admin

from .models import Sala

# Register your models here.

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'bloco', 'andar', 'uso')
    search_fields = ('numero', 'bloco__nome', 'uso')
    list_filter = ('bloco__nome', 'uso')