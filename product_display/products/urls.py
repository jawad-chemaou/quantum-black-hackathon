from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # Associe la vue à la racine de l'application
]

