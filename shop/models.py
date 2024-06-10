from django.db import models
from django.utils import timezone
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to="categorias", null=True)
    
    def __str__(self):
        return self.nombre
    
class Producto (models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()
    precio = models.IntegerField(default=0)
    descripcion = models.TextField(null=True)
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    creado_en = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(upload_to="productos", null=True)
    
    def __str__(self):
        return self.nombre

    
    
class Contacto (models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    mensaje = models.TextField()
    
    def __str__(self):
        return self.nombre
