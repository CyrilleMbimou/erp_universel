def fournisseurs_list(request):
    fournisseurs = Fournisseur.objects.all()
    return render(request, "fournisseurs/fournisseurs_list.html", {"fournisseurs": fournisseurs})

from django.shortcuts import render, redirect
from .models import Fournisseur
from .forms import FournisseurForm

def fournisseurs_list(request):
    fournisseurs = Fournisseur.objects.all()
    return render(request, "fournisseurs/fournisseurs_list.html", {"fournisseurs": fournisseurs})

def fournisseur_create(request):
    if request.method == "POST":
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fournisseurs_list')
    else:
        form = FournisseurForm()
    return render(request, "fournisseurs/fournisseur_form.html", {"form": form})

def fournisseur_edit(request, pk):
    fournisseur = Fournisseur.objects.get(pk=pk)
    if request.method == "POST":
        form = FournisseurForm(request.POST, instance=fournisseur)
        if form.is_valid():
            form.save()
            return redirect('fournisseurs_list')
    else:
        form = FournisseurForm(instance=fournisseur)
    return render(request, "fournisseurs/fournisseur_form.html", {"form": form, "edit": True})

def fournisseur_delete(request, pk):
    fournisseur = Fournisseur.objects.get(pk=pk)
    if request.method == "POST":
        fournisseur.delete()
        return redirect('fournisseurs_list')
    return render(request, "fournisseurs/fournisseur_confirm_delete.html", {"fournisseur": fournisseur})
