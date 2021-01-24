from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.shortcuts import render, reverse
from .models import modeloMascota


# Create your views here.

class Home (CreateView):
    model =  modeloMascota
    template_name = 'index.html'
    fields = '__all__'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        listamascotas = modeloMascota.objects.all()
        context['lista'] = listamascotas
        return context

    def get_success_url(self):
        return reverse('home',kwargs={})
    
class editar(UpdateView):
    model = modeloMascota
    template_name = 'padre.html'
    fields = '__all__'
    success_url = reverse_lazy('home')
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        listamascotas = modeloMascota.objects.all()
        context['lista'] = listamascotas
        return context

class eliminar(DeleteView):
    model = modeloMascota
    template_name = 'padre.html'
    success_url = reverse_lazy('home')
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        listamascotas = modeloMascota.objects.all()
        context['lista'] = listamascotas
        return context