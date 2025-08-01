def produits_list(request):
    produits = Produit.objects.all()
    return render(request, "produits/produits_list.html", {"produits": produits})

from django.shortcuts import render, redirect
from .models import Produit
from .forms import ProduitForm

def produits_list(request):
    produits = Produit.objects.all()
    return render(request, "produits/produits_list.html", {"produits": produits})

def produit_create(request):
    if request.method == "POST":
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produits_list')
    else:
        form = ProduitForm()
    return render(request, "produits/produit_form.html", {"form": form})

def produit_edit(request, pk):
    produit = Produit.objects.get(pk=pk)
    if request.method == "POST":
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('produits_list')
    else:
        form = ProduitForm(instance=produit)
    return render(request, "produits/produit_form.html", {"form": form, "edit": True})

def produit_delete(request, pk):
    produit = Produit.objects.get(pk=pk)
    if request.method == "POST":
        produit.delete()
        return redirect('produits_list')
    return render(request, "produits/produit_confirm_delete.html", {"produit": produit})
