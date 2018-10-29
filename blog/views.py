from django.shortcuts import render
from django.utils import timezone
from .models import Form,Mascota


def Contacto(request):
    estado = False
    autor= Form()
    if request.method=="POST":

    
        autor.correo = request.POST['correo']
        autor.rut = request.POST['rut']
        autor.nombre = request.POST['nombre']
        autor.fecha = request.POST['fecha']
        autor.numero = request.POST['numero']
        autor.region = request.POST['region']
        autor.comuna = request.POST['ciudad']
        autor.vivienda = request.POST['vivienda']
        autor.save()
        estado=True

    dic={ 'estado': estado }
    return render(request, 'blog/Contacto.html', dic)

def Mascotas(request):
    estado = False       
    masc=Mascota()
    if request.method=="POST":

        masc.nombre = request.POST['nombre']
        masc.raza = request.POST['raza']
        masc.descripcion = request.POST['descripcion']
        masc.imagen = request.POST['imagen']
        masc.estado = request.POST['estado']
        masc.save()
        estado=True

    dic={'estado': estado}
    return render(request,'blog/Mascotas.html', dic)
    
# Create your views here.

		