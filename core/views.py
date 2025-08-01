def clients_list(request):
    clients = Client.objects.all()
    return render(request, "core/clients_list.html", {"clients": clients})

from django.shortcuts import render, redirect
from .models import Client
from .forms import ClientForm

def clients_list(request):
    clients = Client.objects.all()
    return render(request, "core/clients_list.html", {"clients": clients})

def client_create(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients_list')
    else:
        form = ClientForm()
    return render(request, "core/client_form.html", {"form": form})

def client_edit(request, pk):
    client = Client.objects.get(pk=pk)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('clients_list')
    else:
        form = ClientForm(instance=client)
    return render(request, "core/client_form.html", {"form": form, "edit": True})

def client_delete(request, pk):
    client = Client.objects.get(pk=pk)
    if request.method == "POST":
        client.delete()
        return redirect('clients_list')
    return render(request, "core/client_confirm_delete.html", {"client": client})
