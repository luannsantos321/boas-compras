from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('lista/', views.lista, name='lista'),
    path('submit/', views.cadastro, name='cadastro'),
]