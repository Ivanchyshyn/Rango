from django.views.generic import DetailView, ListView, RedirectView, TemplateView
from django.shortcuts import render
from .models import Category, Page

class IndexView(ListView):
    #queryset = Category.objects.order_by('-likes')[:5]
    model = Category
    template_name = 'rango/index.html'
    context_object_name = 'categories'
    extra_context = {'pages': Page.objects.order_by('-views')[:5]}

    def get_queryset(self):
        return self.model._default_manager.order_by('-likes')[:5]

class CategoryView(ListView):
    model = Category
    context_object_name = 'categories'

    def get_queryset(self):
        return self.model._default_manager.order_by('-likes')

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'rango/category_detail.html'

class AboutRangoView(TemplateView):
    extra_context = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    template_name = 'rango/about.html'

class IndexRedirectView(RedirectView):
    url = 'rango/'
    permanent = True