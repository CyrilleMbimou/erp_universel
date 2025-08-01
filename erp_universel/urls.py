"""
URL configuration for erp_universel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path




from core.views import clients_list, client_create, client_edit, client_delete
from ventes.views import ventes_list, vente_create, vente_edit, vente_delete
from produits.views import produits_list, produit_create, produit_edit, produit_delete
from stocks.views import stocks_list, stock_create, stock_edit, stock_delete
from fournisseurs.views import fournisseurs_list, fournisseur_create, fournisseur_edit, fournisseur_delete
from achats.views import achats_list, achat_create, achat_edit, achat_delete
from comptabilite.views import compta_list, ecriture_create, ecriture_edit, ecriture_delete
from rh.views import employes_list, employe_create, employe_edit, employe_delete
from projets.views import projets_list, projet_create, projet_edit, projet_delete
from documents.views import documents_list, document_create, document_edit, document_delete
from dashboard.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('clients/', clients_list, name='clients_list'),
    path('clients/ajouter/', client_create, name='client_create'),
    path('clients/<int:pk>/modifier/', client_edit, name='client_edit'),
    path('clients/<int:pk>/supprimer/', client_delete, name='client_delete'),
    path('ventes/', ventes_list, name='ventes_list'),
    path('ventes/ajouter/', vente_create, name='vente_create'),
    path('ventes/<int:pk>/modifier/', vente_edit, name='vente_edit'),
    path('ventes/<int:pk>/supprimer/', vente_delete, name='vente_delete'),
    path('produits/', produits_list, name='produits_list'),
    path('produits/ajouter/', produit_create, name='produit_create'),
    path('produits/<int:pk>/modifier/', produit_edit, name='produit_edit'),
    path('produits/<int:pk>/supprimer/', produit_delete, name='produit_delete'),
    path('stocks/', stocks_list, name='stocks_list'),
    path('stocks/ajouter/', stock_create, name='stock_create'),
    path('stocks/<int:pk>/modifier/', stock_edit, name='stock_edit'),
    path('stocks/<int:pk>/supprimer/', stock_delete, name='stock_delete'),
    path('fournisseurs/', fournisseurs_list, name='fournisseurs_list'),
    path('fournisseurs/ajouter/', fournisseur_create, name='fournisseur_create'),
    path('fournisseurs/<int:pk>/modifier/', fournisseur_edit, name='fournisseur_edit'),
    path('fournisseurs/<int:pk>/supprimer/', fournisseur_delete, name='fournisseur_delete'),
    path('achats/', achats_list, name='achats_list'),
    path('achats/ajouter/', achat_create, name='achat_create'),
    path('achats/<int:pk>/modifier/', achat_edit, name='achat_edit'),
    path('achats/<int:pk>/supprimer/', achat_delete, name='achat_delete'),
    path('comptabilite/', compta_list, name='compta_list'),
    path('comptabilite/ajouter/', ecriture_create, name='ecriture_create'),
    path('comptabilite/<int:pk>/modifier/', ecriture_edit, name='ecriture_edit'),
    path('comptabilite/<int:pk>/supprimer/', ecriture_delete, name='ecriture_delete'),
    path('employes/', employes_list, name='employes_list'),
    path('employes/ajouter/', employe_create, name='employe_create'),
    path('employes/<int:pk>/modifier/', employe_edit, name='employe_edit'),
    path('employes/<int:pk>/supprimer/', employe_delete, name='employe_delete'),
    path('projets/', projets_list, name='projets_list'),
    path('projets/ajouter/', projet_create, name='projet_create'),
    path('projets/<int:pk>/modifier/', projet_edit, name='projet_edit'),
    path('projets/<int:pk>/supprimer/', projet_delete, name='projet_delete'),
    path('documents/', documents_list, name='documents_list'),
    path('documents/ajouter/', document_create, name='document_create'),
    path('documents/<int:pk>/modifier/', document_edit, name='document_edit'),
    path('documents/<int:pk>/supprimer/', document_delete, name='document_delete'),
]
