from django.db import models
from  django.contrib.auth.models import User
from django.db.models.signals import post_save

#PERFIL DE USUARIO

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    image = models.ImageField(upload_to='profile_images/', default='default.jpg', verbose_name='Imagen de perfil')
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name='Dirección')
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='Número de teléfono')
    location = models.CharField(max_length=100, blank=True, null=True, verbose_name='Localidad')
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['-id']
        
    def __str__(self):
        return self.user.username
    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)