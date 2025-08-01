def compta_list(request):
    ecritures = EcritureComptable.objects.all()
    return render(request, "comptabilite/compta_list.html", {"ecritures": ecritures})

from django.shortcuts import render, redirect
from .models import EcritureComptable
from .forms import EcritureComptableForm

def compta_list(request):
    ecritures = EcritureComptable.objects.all()
    return render(request, "comptabilite/compta_list.html", {"ecritures": ecritures})

def ecriture_create(request):
    if request.method == "POST":
        form = EcritureComptableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('compta_list')
    else:
        form = EcritureComptableForm()
    return render(request, "comptabilite/ecriture_form.html", {"form": form})

def ecriture_edit(request, pk):
    ecriture = EcritureComptable.objects.get(pk=pk)
    if request.method == "POST":
        form = EcritureComptableForm(request.POST, instance=ecriture)
        if form.is_valid():
            form.save()
            return redirect('compta_list')
    else:
        form = EcritureComptableForm(instance=ecriture)
    return render(request, "comptabilite/ecriture_form.html", {"form": form, "edit": True})

def ecriture_delete(request, pk):
    ecriture = EcritureComptable.objects.get(pk=pk)
    if request.method == "POST":
        ecriture.delete()
        return redirect('compta_list')
    return render(request, "comptabilite/ecriture_confirm_delete.html", {"ecriture": ecriture})
