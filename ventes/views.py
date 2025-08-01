def ventes_list(request):
    ventes = Vente.objects.select_related('client').all()
    return render(request, "ventes/ventes_list.html", {"ventes": ventes})

from django.shortcuts import render, redirect
from .models import Vente
from .forms import VenteForm

def ventes_list(request):
    ventes = Vente.objects.select_related('client').all()
    return render(request, "ventes/ventes_list.html", {"ventes": ventes})

def vente_create(request):
    if request.method == "POST":
        form = VenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ventes_list')
    else:
        form = VenteForm()
    return render(request, "ventes/vente_form.html", {"form": form})

def vente_edit(request, pk):
    vente = Vente.objects.get(pk=pk)
    if request.method == "POST":
        form = VenteForm(request.POST, instance=vente)
        if form.is_valid():
            form.save()
            return redirect('ventes_list')
    else:
        form = VenteForm(instance=vente)
    return render(request, "ventes/vente_form.html", {"form": form, "edit": True})

def vente_delete(request, pk):
    vente = Vente.objects.get(pk=pk)
    if request.method == "POST":
        vente.delete()
        return redirect('ventes_list')
    return render(request, "ventes/vente_confirm_delete.html", {"vente": vente})
