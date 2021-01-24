from django.urls import path
from .views import Home, editar, eliminar

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('home/', Home.as_view(), name='home'),
    path('editar/<int:pk>',editar.as_view(), name='editar'),
    path('eliminar/<int:pk>',eliminar.as_view(), name='eliminar'),
    
]