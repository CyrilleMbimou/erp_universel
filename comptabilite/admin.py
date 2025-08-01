from django.contrib import admin
from .models import EcritureComptable

@admin.register(EcritureComptable)
class EcritureComptableAdmin(admin.ModelAdmin):
    list_display = ("date", "libelle", "montant", "type")
    search_fields = ("libelle",)
    list_filter = ("type", "date")
