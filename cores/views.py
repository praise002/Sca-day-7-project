from django.shortcuts import render
from django.urls import reverse_lazy
from . models import Core
from django.views.generic import ListView, DetailView, UpdateView, CreateView


class IndexView(ListView):  #display all item from db
    model = Core
    template_name = 'core/index.html'
    context_object_name = 'index'  #default is model_list
    
    
class SingleView(DetailView):  #take one item from d db
    model = Core
    template_name = 'core/single.html'
    context_object_name = 'post'


class PostView(ListView):
    model = Core
    template_name = 'core/posts.html'
    context_object_name = 'posst_list'
    
class AddView(CreateView):
    model = Core
    template_name = 'core/add.html'
    fields = '__all__'
    success_url = reverse_lazy('cores:posts')