from django.db import models

# Create your models here.
class Campistas(models.Model):
    id_camp=models.AutoField(primary_key=True)
    nombre_camp= models.CharField(max_length=100, null=False, blank=False)
    apell_camp = models.CharField(max_length=100, null=False, blank=False)
    correo_camp = models.EmailField(null=False, blank=False)
    telef_camp = models.CharField(max_length=10, null=False, blank=False)
    cedula_camp = models.CharField(max_length=10, null=False, blank=False)
    direcc_camp = models.TextField(null=False, blank=False)

class Reservas(models.Model):
    TIPO_ALOJAMIENTO = [
        ('Tienda','Tienda'),
        ('Cabaña','Cabaña'),
        ('Caravana','Caravana')
    ]
    ESTADO_RESERVA = [
        ('Confirmada','Confirmada'),
        ('Pendiente','Pendiente'),
        
    ]
    id_rev=models.AutoField(primary_key=True)
    fechain_rev=models.DateField(null=False, blank=False)
    fechfin_rev=models.DateField(null=False, blank=False)
    tipaloj_rev=models.CharField(max_length=20, choices=TIPO_ALOJAMIENTO, default='Tienda')
    numpers_rev = models.CharField(max_length=200, null=False, blank=False)
    estado_rev=models.CharField(max_length=20, choices=ESTADO_RESERVA, default='Confirmada')
    campista = models.ForeignKey(Campistas, on_delete=models.CASCADE, related_name="campistas")
    obser_rev= models.TextField(max_length=500,null=False, blank=False )
    
    
    