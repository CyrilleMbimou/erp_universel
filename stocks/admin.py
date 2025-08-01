from django.contrib import admin
from .models import Stock

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ("produit", "quantite", "seuil_alerte")
    search_fields = ("produit__nom", "produit__reference")
    list_filter = ("quantite",)
