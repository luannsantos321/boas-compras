from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('lista/', views.lista, name='lista'),
    path('update/<int:id>/', views.update_cadastro, name='update_cadastro'),
    path('delete/<int:id>/', views.delete_cadastro, name='delete_cadastro')
]
