from django.shortcuts import render, redirect, get_object_or_404
from .models import Campistas
from .models import Reservas
from django.contrib import messages
# Create your views here.
def inicio(request):
    return render (request,'inicio.html')

#Campistas
def nuevoCampista(request):
    campista = Campistas.objects.all()
    return render (request,'nuevoCampista.html',{
        'campista': campista
    })

def listadoCampista(request):
    campistaBdd=Campistas.objects.all()
    return render(request,'listadoCampista.html',{'campista':campistaBdd})

def guardarCampista(request):
    nombre_camp=request.POST['txt_nombre_camp']
    apell_camp=request.POST['txt_apell_camp']
    correo_camp=request.POST['txt_correo_camp']
    telef_camp=request.POST['txt_telef_camp']
    cedula_camp=request.POST['txt_cedla_camp']
    direcc_camp=request.POST['txt_direcc_camp']
    nuevoCampista=Campistas.objects.create(nombre_camp=nombre_camp,
                                           apell_camp=apell_camp, correo_camp=correo_camp,
                                           telef_camp=telef_camp, cedula_camp=cedula_camp,
                                           direcc_camp=direcc_camp)
    
    messages.success(request,"Se ha guardado el Campista")
    return redirect('/listadoCampista')

def eliminarCampista(request, id_camp):
    campistaEliminar=get_object_or_404(Campistas, id_camp=id_camp)
    campistaEliminar.delete()
    messages.success(request,"Campista Eliminado")
    return redirect('/listadoCampista')

def editarCampista(request,id_camp):
    campistaEditar=Campistas.objects.get(id_camp=id_camp)
    return render(request,'editarCampista.html',
                    {'campista':campistaEditar})

def procesarEdicionCampista(request):
    campista=Campistas.objects.get(id_camp=request.POST['id_camp'])
    campista.nombre_camp=request.POST['txt_nombre_camp']
    campista.apell_camp=request.POST['txt_apell_camp']
    campista.correo_camp=request.POST['txt_correo_camp']
    campista.telef_camp=request.POST['txt_telef_camp']
    campista.cedula_camp=request.POST['txt_cedla_camp']
    campista.direcc_camp=request.POST['txt_direcc_camp']
    
    campista.save()
    messages.success(request,"Campista actualizado con exito")
    return redirect('/listadoCampista')


#Reservas

def nuevoReservas(request):
    campistas = Campistas.objects.all()
    return render(request, 'nuevoReservas.html', {
        'campista': campistas
    })

def listadoReservas(request):
    reservasBdd = Reservas.objects.all()
    campistaBdd = Campistas.objects.all()
    return render(request, 'listadoReservas.html', {'reserva': reservasBdd, 'campista': campistaBdd})


def guardarReserva(request):
    fechain_rev = request.POST['txt_fechin_rev']
    fechfin_rev = request.POST['txt_fechfin_rev']
    tipaloj_rev = request.POST['txt_tipoaloj_camp']
    numpers_rev = request.POST['txt_numper_rev']
    estado_rev = request.POST['txt_estado_rev']
    id_camp = request.POST['id_camp']
    obser_rev = request.POST['txt_obsrv_rev']
    
    campista = get_object_or_404(Campistas, id_camp=id_camp)
    
    nuevoReservas = Reservas.objects.create(
        fechain_rev=fechain_rev,
        fechfin_rev=fechfin_rev,
        tipaloj_rev=tipaloj_rev,
        numpers_rev=numpers_rev,
        estado_rev=estado_rev,
        campista=campista,
        obser_rev=obser_rev
    )
    
    messages.success(request, "Se ha guardado la reserva")
    return redirect('/listadoReservas')

def eliminarReserva(request, id_rev):
    reservaEliminar = get_object_or_404(Reservas, id_rev=id_rev)
    reservaEliminar.delete()
    messages.success(request, "Reserva eliminada")
    return redirect('/listadoReservas')

def editarReserva(request, id_rev):
    reservaEditar = get_object_or_404(Reservas, id_rev=id_rev)
    campistas = Campistas.objects.all()
    return render(request, 'editarReservas.html', {
        'reserva': reservaEditar,
        'campistas': campistas
    })

def procesarEdicionReserva(request):
    reserva = Reservas.objects.get(id_rev=request.POST['id_rev'])
    reserva.fechain_rev = request.POST['fechain_rev']
    reserva.fechfin_rev = request.POST['fechfin_rev']
    reserva.tipaloj_rev = request.POST['tipaloj_rev']
    reserva.numpers_rev = request.POST['numpers_rev']
    reserva.estado_rev = request.POST['estado_rev']
    
    
    id_camp = request.POST['campista']
    reserva.campista = get_object_or_404(Campistas, id_camp=id_camp)
    
    reserva.obser_rev = request.POST['obser_rev']
    
    reserva.save()
    messages.success(request, "Reserva actualizada con éxito")
    return redirect('/listadoReservas')
