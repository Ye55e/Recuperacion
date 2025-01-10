from django.urls import path
from . import views
urlpatterns = [
    path('',views.inicio, name='inicio'),
    #Campistas
    path('nuevoCampista/',views.nuevoCampista,name='nuevoCampista'),
    path('listadoCampista/',views.listadoCampista, name='listadoCampista'),
    path('guardarCampista/',views.guardarCampista, name='guardarCampista'),
    path('eliminarCampista/<id_camp>', views.eliminarCampista, name='eliminarCampista'),
    path('editarCampista/<id_camp>',views.editarCampista, name='editarCampista'),
    path('procesarEdicionCampista/',views.procesarEdicionCampista, name='procesarEdicionCampista'),
    
    #Reservas
    path('nuevoReservas/',views.nuevoReservas,name='nuevoReservas'),
    path('listadoReservas/',views.listadoReservas, name='listadoReservas'),
    path('guardarReserva/',views.guardarReserva, name='guardarReserva'),
    path('eliminarReserva/<id_rev>', views.eliminarReserva, name='eliminarReserva'),
    path('editarReserva/<id_rev>',views.editarReserva, name='editarReserva'),
    path('procesarEdicionReserva/',views.procesarEdicionReserva, name='procesarEdicionReserva')
    
]