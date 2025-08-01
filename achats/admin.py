from django.contrib import admin
from .models import Achat

@admin.register(Achat)
class AchatAdmin(admin.ModelAdmin):
    list_display = ("produit", "fournisseur", "date_achat", "quantite", "prix_unitaire")
    search_fields = ("produit__nom", "fournisseur__nom")
    list_filter = ("date_achat",)
