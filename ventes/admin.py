from django.contrib import admin
from .models import Vente

@admin.register(Vente)
class VenteAdmin(admin.ModelAdmin):
    list_display = ("id", "client", "date_vente", "montant")
    search_fields = ("client__nom", "client__prenom")
    list_filter = ("date_vente",)
