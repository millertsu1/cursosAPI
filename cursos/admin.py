from django.contrib import admin
from .models import Curso, Categoria

class CursosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'duracion', 'price')
    search_fields = ('nombre', 'creador__username')
    list_filter = ('categorias', 'puntuacion')
    


admin.site.register(Curso, CursosAdmin)
admin.site.register(Categoria)

