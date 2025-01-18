from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages


# Create your views here.
def index(request):
    categories = Category.objects.all()
        
# Paginate the combined reviews

    paginator = Paginator(categories, 8)  # Show 8 reviews per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

# Pass the paginated reviews to the template

    context = {
        'categories_list': page_obj,
        'is_paginated': page_obj.has_other_pages(),
    }
    print(page_obj)
    return render(request, 'shop/index.html', context)

def product(request, product_id):
    product_query = get_object_or_404(Product, id=product_id)
    # # reviews = product.ratings.all().order_by("-created_at")
    # # rating_count = product.ratings.count()
    # # avg_rating = product.ratings.aggregate(Avg('rating'))['rating__avg'] or 0
    # # stars = range(1, 6)
    # # user_rating = None
    # # rating_form = None

    # if request.user.is_authenticated:
    #     user_rating = Rating.objects.filter(product=product, user=request.user).first()
    # if request.user.is_authenticated:
    #     user_rating = Rating.objects.filter(product=product, user=request.user).first()
        
    #     if request.method == "POST":
    #         if user_rating:
    #             messages.info(request, "You've already reviewd this product. You can't submit another review.")
    #         else:
    #             rating_form = RatingForm(data=request.POST)
    #             if rating_form.is_valid():
    #                 rating = rating_form.save(commit=False)
    #                 rating.product = product
    #                 rating.user = request.user
    #                 rating.save()
    #                 messages.success(request, 'Your rating has been submitted successfully!')
    #         return redirect('shop:product', product_id = product_id)
    #     else:
    #         rating_form = RatingForm() if not user_rating else None
    #     if request.method == "POST":
    #         if user_rating:
    #             messages.info(request, "You've already reviewd this product. You can't submit another review.")
    #         else:
    #             rating_form = RatingForm(data=request.POST)
    #             if rating_form.is_valid():
    #                 rating = rating_form.save(commit=False)
    #                 rating.product = product
    #                 rating.user = request.user
    #                 rating.save()
    #                 messages.success(request, 'Your rating has been submitted successfully!')
    #         return redirect('shop:product', product_id = product_id)
    #     else:
    #         rating_form = RatingForm() if not user_rating else None
    return render(request, "shop/product.html", {"product": product_query})

def category(request, category_id):

    # cat=Category.select_related("products")
    category = get_object_or_404(Category, id=category_id)
    
    return render(request, 'shop/category.html', {
        'category': category,
    })

def view_cart(request):
    order = Order.objects.filter(customer=request.user, order_date__isnull=True).first()
    if not order:
        return HttpResponse("Your cart is empty.")
    order_products = OrderProduct.objects.filter(order=order)
    total = sum(order_product.product.price * order_product.quantity for order_product in order_products)
    return render(request, 'shop/cart.html', {
        'order': order,
        'order_products': order_products,
        'total': total,
    })

# remove product from cart
def remove_from_cart(request, order_product_id):
    order_product = get_object_or_404(OrderProduct, id=order_product_id)
    order_product.delete()
    return redirect('cart')

def view_wishlist(request):
    wishlist_items = Wishlist.objects.filter(customer=request.user)
    return render(request, 'shop/wishlist.html', {
        'wishlist_items': wishlist_items,
    })

def remove_from_wishlist(request, wishlist_id):
    wishlist_item = get_object_or_404(Wishlist, id=wishlist_id)
    wishlist_item.delete()
    return redirect('wishlist')

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if not Wishlist.objects.filter(customer=request.user, product=product).exists():
        Wishlist.objects.create(customer=request.user, product=product)
    return redirect('product')

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    messages.add_message(request, messages.SUCCESS, "Added {name} to basket!".format(name = product.name))

    order = Order.objects.filter(customer=request.user, order_date__isnull=True).first()
    order_product = OrderProduct.objects.filter(order = order, product = product).first()
    if order_product:
        order_product.quantity = order_product.quantity + 1
    else:
        order_product = OrderProduct.objects.create(order = order, product = product, quantity = 1)
    
    order_product.save()

    return redirect("category", product.category.id)
