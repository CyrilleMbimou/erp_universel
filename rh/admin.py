from django.contrib import admin
from .models import Employe

@admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ("nom", "prenom", "poste", "date_embauche")
    search_fields = ("nom", "prenom", "poste")
