def documents_list(request):
    documents = Document.objects.all()
    return render(request, "documents/documents_list.html", {"documents": documents})

from django.shortcuts import render, redirect
from .models import Document
from .forms import DocumentForm

def documents_list(request):
    documents = Document.objects.all()
    return render(request, "documents/documents_list.html", {"documents": documents})

def document_create(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('documents_list')
    else:
        form = DocumentForm()
    return render(request, "documents/document_form.html", {"form": form})

def document_edit(request, pk):
    document = Document.objects.get(pk=pk)
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES, instance=document)
        if form.is_valid():
            form.save()
            return redirect('documents_list')
    else:
        form = DocumentForm(instance=document)
    return render(request, "documents/document_form.html", {"form": form, "edit": True})

def document_delete(request, pk):
    document = Document.objects.get(pk=pk)
    if request.method == "POST":
        document.delete()
        return redirect('documents_list')
    return render(request, "documents/document_confirm_delete.html", {"document": document})
