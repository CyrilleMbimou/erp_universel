def employes_list(request):
    employes = Employe.objects.all()
    return render(request, "rh/employes_list.html", {"employes": employes})

from django.shortcuts import render, redirect
from .models import Employe
from .forms import EmployeForm

def employes_list(request):
    employes = Employe.objects.all()
    return render(request, "rh/employes_list.html", {"employes": employes})

def employe_create(request):
    if request.method == "POST":
        form = EmployeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employes_list')
    else:
        form = EmployeForm()
    return render(request, "rh/employe_form.html", {"form": form})

def employe_edit(request, pk):
    employe = Employe.objects.get(pk=pk)
    if request.method == "POST":
        form = EmployeForm(request.POST, instance=employe)
        if form.is_valid():
            form.save()
            return redirect('employes_list')
    else:
        form = EmployeForm(instance=employe)
    return render(request, "rh/employe_form.html", {"form": form, "edit": True})

def employe_delete(request, pk):
    employe = Employe.objects.get(pk=pk)
    if request.method == "POST":
        employe.delete()
        return redirect('employes_list')
    return render(request, "rh/employe_confirm_delete.html", {"employe": employe})
