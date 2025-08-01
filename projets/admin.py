from django.contrib import admin
from .models import Projet

@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ("nom", "statut", "date_debut", "date_fin")
    search_fields = ("nom",)
    list_filter = ("statut",)
