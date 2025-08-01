def projets_list(request):
    projets = Projet.objects.all()
    return render(request, "projets/projets_list.html", {"projets": projets})

from django.shortcuts import render, redirect
from .models import Projet
from .forms import ProjetForm

def projets_list(request):
    projets = Projet.objects.all()
    return render(request, "projets/projets_list.html", {"projets": projets})

def projet_create(request):
    if request.method == "POST":
        form = ProjetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projets_list')
    else:
        form = ProjetForm()
    return render(request, "projets/projet_form.html", {"form": form})

def projet_edit(request, pk):
    projet = Projet.objects.get(pk=pk)
    if request.method == "POST":
        form = ProjetForm(request.POST, instance=projet)
        if form.is_valid():
            form.save()
            return redirect('projets_list')
    else:
        form = ProjetForm(instance=projet)
    return render(request, "projets/projet_form.html", {"form": form, "edit": True})

def projet_delete(request, pk):
    projet = Projet.objects.get(pk=pk)
    if request.method == "POST":
        projet.delete()
        return redirect('projets_list')
    return render(request, "projets/projet_confirm_delete.html", {"projet": projet})
