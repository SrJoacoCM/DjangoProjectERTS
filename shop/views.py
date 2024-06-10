from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from .forms import ContactoForm, ProductoForm
from .models import Producto
from django.core.paginator import Paginator
from django.contrib import messages


# Create your views here.

def index (request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(productos, 10)
        productos = paginator.page(page)
    except:
        raise Http404
    
    data = {
        'entity': productos,
        'paginator': paginator,
        
    }
    return render(
        request,
        'index.html',
        context={
            'productos': productos,
            'paginator': paginator}
    )



def detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto = Producto.objects.get(id=producto_id)
        
    return render(
        request, 
        'detalle.html', 
        context= {'producto': producto})
    

    
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
           messages.success(request, "Agregado Correctamente")
        else:
            data["form"] = formulario
    
    return render(request,'producto/agregar.html', data)

def modificar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    data = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
           formulario.save()
           messages.success(request, "Modificado Correctamente")
           return HttpResponseRedirect('/shop')
        else:
            data["form"] = formulario
    
    return render(request, 'producto/modificar.html',data)

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado Correctamente")
    return HttpResponseRedirect('/shop')
    