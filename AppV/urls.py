from django.urls import path
from AppV import views


urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('clientes/', views.clientes, name='clientes'),
    path('proveedores/', views.proveedores, name='proveedores'),
    path('vendedores/', views.vendedores, name='vendedores'), 
    path('expresos/', views.expresos, name='expresos'),  
    path('buscar_cliente/', views.buscar_cliente, name='buscar_cliente'),
]
