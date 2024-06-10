from django import forms
from . import models
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm

class ProductoForm(ModelForm):
    class Meta:
        model = models.Producto
        fields = ['nombre', 'stock', 'precio', 'categoria','descripcion' , 'imagen',]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        
class ContactoForm(ModelForm):
    class Meta:
        model = models.Contacto
        fields = ['nombre', 'correo', 'mensaje',]
        widgets = {
             'nombre': forms.TextInput(attrs={'class': 'form-control'}),
             'correo': forms.TextInput(attrs={'class': 'form-control'}),
             'mensaje': forms.Textarea(attrs={'class': 'form-control'}),
         }
        
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))