from django.urls import path
from .views import IndexView, AboutRangoView, CategoryView, CategoryDetailView

app_name = 'rango'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutRangoView.as_view(), name='about'),
    path('category/', CategoryView.as_view(), name='category'),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
]