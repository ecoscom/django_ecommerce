from django.shortcuts import render
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

def product_detail_view(request):
    pass