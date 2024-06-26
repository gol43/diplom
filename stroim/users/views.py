from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CreationForm
from django.urls import reverse_lazy

class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('products:index')
    template_name = 'users/signup.html'
