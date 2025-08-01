from django import forms
from .models import Employe

class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = ['nom', 'prenom', 'poste', 'email', 'telephone', 'date_embauche']
