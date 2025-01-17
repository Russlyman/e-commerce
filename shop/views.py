from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *


# Create your views here.
def index(request):
    categories = Category.objects.all()
    return render(request, "shop/index.html", {"categories": categories})

def product(request, product_id):
    product_query = get_object_or_404(Product, id=product_id)
    # reviews = product.ratings.all().order_by("-created_at")
    # rating_count = product.ratings.count()
    # avg_rating = product.ratings.aggregate(Avg('rating'))['rating__avg'] or 0
    # stars = range(1, 6)
    # user_rating = None
    # rating_form = None

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
    return render(request, "shop/product.html", {"product": product_query})

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    
    return render(request, 'shop/category.html', {
        'category': category,
    })