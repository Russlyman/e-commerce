from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *


# Create your views here.
def index(request):
    return render(request, "shop/index.html")

def product(request, product_id):
    product_query = get_object_or_404(Product, id=product_id)
    return render(request, "shop/product.html", {"product": product_query})

def item_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all() 
    
    return render(request, 'shop/product.html', {
        'category': category,
        'products': products,
    })