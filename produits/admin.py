from django.contrib import admin
from .models import Produit

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ("nom", "reference", "prix_unitaire")
    search_fields = ("nom", "reference")
