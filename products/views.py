from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Product

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'

    def get_context_data(self, *args, **kwargs):
        return super(ProductListView, self).get_context_data(*args, **kwargs)

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
        
         

def product_detail_view(request):
    pass