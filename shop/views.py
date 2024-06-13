from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from .forms import ContactoForm, ProductoForm, CustomUserCreationForm
from .models import Producto
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.


@permission_required('shop.view_producto')
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




@permission_required('shop.add_producto')
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



@permission_required('shop.change_producto')
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



@permission_required('shop.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado Correctamente")
    return HttpResponseRedirect('/shop')
    
    
def registro (request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username= formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registrado Correctamente")
            return redirect(to="inicio")
        data['form'] = formulario
    return render(request, 'registration/registro.html', data)