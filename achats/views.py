def achats_list(request):
    achats = Achat.objects.select_related('fournisseur', 'produit').all()
    return render(request, "achats/achats_list.html", {"achats": achats})

from django.shortcuts import render, redirect
from .models import Achat
from .forms import AchatForm

def achats_list(request):
    achats = Achat.objects.select_related('fournisseur', 'produit').all()
    return render(request, "achats/achats_list.html", {"achats": achats})

def achat_create(request):
    if request.method == "POST":
        form = AchatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('achats_list')
    else:
        form = AchatForm()
    return render(request, "achats/achat_form.html", {"form": form})

def achat_edit(request, pk):
    achat = Achat.objects.get(pk=pk)
    if request.method == "POST":
        form = AchatForm(request.POST, instance=achat)
        if form.is_valid():
            form.save()
            return redirect('achats_list')
    else:
        form = AchatForm(instance=achat)
    return render(request, "achats/achat_form.html", {"form": form, "edit": True})

def achat_delete(request, pk):
    achat = Achat.objects.get(pk=pk)
    if request.method == "POST":
        achat.delete()
        return redirect('achats_list')
    return render(request, "achats/achat_confirm_delete.html", {"achat": achat})
