from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm

def stocks_list(request):
    stocks = Stock.objects.select_related('produit').all()
    return render(request, "stocks/stocks_list.html", {"stocks": stocks})

def stock_create(request):
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stocks_list')
    else:
        form = StockForm()
    return render(request, "stocks/stock_form.html", {"form": form})

def stock_edit(request, pk):
    stock = Stock.objects.get(pk=pk)
    if request.method == "POST":
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect('stocks_list')
    else:
        form = StockForm(instance=stock)
    return render(request, "stocks/stock_form.html", {"form": form, "edit": True})

def stock_delete(request, pk):
    stock = Stock.objects.get(pk=pk)
    if request.method == "POST":
        stock.delete()
        return redirect('stocks_list')
    return render(request, "stocks/stock_confirm_delete.html", {"stock": stock})
