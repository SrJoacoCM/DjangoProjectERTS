from . import models
from django.forms import ModelForm

class ProductoForm(ModelForm):
    class Meta:
        model = models.Producto
        fields = ['nombre', 'stock', 'precio', 'categoria', 'imagen',]
        
class ContactoForm(ModelForm):
    class Meta:
        model = models.Contacto
        fields = ['nombre', 'correo', 'mensaje',]