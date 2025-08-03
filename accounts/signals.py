from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile

@receiver(post_save, sender=Profile)

def add_user_to_students_group(sender, instance, created, **kwargs):
    if created:
        try:
            students_group = Group.objects.get(name='Estudiante')
            
        except Group.DoesNotExist:
            students_group = Group.objects.create(name='Estudiante')
            students_group = Group.objects.create(name='Profesor')
            students_group = Group.objects.create(name='Tutor')
            students_group = Group.objects.create(name='Administrador')
            
        instance.user.groups.add(students_group)