from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CursoViewSet, CategoriaViewSet

router = DefaultRouter()
router.register(r'cursos', CursoViewSet)
router.register(r'categorias', CategoriaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
