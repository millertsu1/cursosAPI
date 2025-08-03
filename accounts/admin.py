from django.contrib import admin
from .models import Profile

#PROFILE DETALLADO
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'address', 'phone_number', 'location','user_group')
    search_fields = ('user__username', 'location', 'user__groups__name')
    list_filter = ('user__groups', 'location')
    
    def user_group(self, obj):
        return " - ".join([t.name for t in obj.user.groups.all().order_by('name')])

    user_group.short_description = 'Grupos de usuario'

class CursosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'creador', 'duracion', 'puntuacion', 'price')
    search_fields = ('nombre', 'creador__username')
    list_filter = ('categorias', 'puntuacion')
    
admin.site.register(Profile, ProfileAdmin)

