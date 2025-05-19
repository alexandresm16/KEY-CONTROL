from django.contrib import admin

from .models import ChaveSala

# Register your models here.

@admin.register(ChaveSala)
class ChaveSalaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'sala')
    search_fields = ('codigo', 'sala__numero')
    list_filter = ('sala__bloco', )