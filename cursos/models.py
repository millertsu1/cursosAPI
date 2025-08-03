from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fragmento = models.TextField(help_text="Descripción corta para las tarjetas de los cursos")
    categorias = models.ManyToManyField(Categoria)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    duracion = models.PositiveIntegerField(help_text="Duración en minutos")
    puntuacion = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)], help_text="Puntuación de 1 a 5 estrellas")
    imagen = models.ImageField(upload_to='cursos_imagenes/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, help_text="Precio del curso en USD")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created'] 
        
    
    
    def __str__(self):
        return self.nombre