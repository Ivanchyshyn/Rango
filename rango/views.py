from django.views.generic import CreateView, DetailView, ListView, RedirectView, TemplateView
from django.shortcuts import render, get_object_or_404
from .models import Category, Page
from .forms import CategoryForm, PageForm


class IndexView(ListView):
    model = Category
    template_name = 'rango/index.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        kwargs['pages'] = Page.objects.order_by('-views')[:5]
        return super().get_context_data(**kwargs)

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


class AddCategoryView(CreateView):
    form_class = CategoryForm
    template_name = 'rango/add_category.html'


class AddPageView(CreateView):
    form_class = PageForm
    template_name = 'rango/add_page.html'

    def form_valid(self, form):
        form.instance.category = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        return super().form_valid(form)


class AboutRangoView(TemplateView):
    extra_context = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    template_name = 'rango/about.html'


class IndexRedirectView(RedirectView):
    url = 'rango/'
    permanent = True
