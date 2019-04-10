from django.views.generic import ListView
from django.shortcuts import render
from .models import Category

class Index(ListView):
    model = Category
    template_name = 'rango/index.html'

def about(request):
    context = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/about.html', context)