from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('login/',login,name='LOGIN'),
    path('cerrar_session/',cerrar_session,name='LOGOUT'),
    path('',menu,name='MENU'),
    path('formulario/',formulario,name='FORMU'),
    path('carrito/',carrito,name='CARRI'),
    path('agregar_carro/<id>/',carro_compras,name='AGREGAR_CARRO'),
    path('carro_mas/<id>/',carro_compras_mas,name='CARRO_MAS'),
    path('carro_menos/<id>/',carro_compras_menos,name='CARRO_MENOS'),
    path('grabar_carro/',grabar_carro,name='GRABAR_CARRO'),
    path('guardar-token/',guardar_token, name='guardar_token'),
]