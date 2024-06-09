from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404

from .forms import ContactoForm, ProductoForm
from .models import Producto


# Create your views here.

def index (request):
    productos = Producto.objects.all()
    
    return render(
        request,
        'index.html',
        context={'productos': productos}
    )



def detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto = Producto.objects.get(id=producto_id)
        
    return render(
        request, 
        'detalle.html', 
        context= {'producto': producto})
    

def formulario(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop:formulario_exitoso')  # Redirigir a alguna página de éxito
    else:
        form = ProductoForm()
    return render(request, 'producto_form.html', {'form': form})
    
def stickers(request):
    productos = Producto.objects.filter(categoria_id=1)
    return render(request, 'stickers.html', {'productos': productos})

def llantas(request):
    productos = Producto.objects.filter(categoria_id=2)
    return render(request, 'llantas.html', {'productos': productos})

def accesorios(request):
    productos = Producto.objects.filter(categoria_id=3)
    return render(request, 'accesorios.html', {'productos': productos})

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/shop/contacto')  
    else:
        form = ContactoForm()

    data = {
        'contacto_form': form
    }
    return render(request, 'contacto.html', data)

def tienda(request):

    return render(request, 'tienda.html')


def agregar_producto (request):
    data= {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
           formulario.save()
        else:
            data["form"] = formulario
    
    return render(request,'producto/agregar.html', data)