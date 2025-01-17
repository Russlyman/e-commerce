from . import views
from django.urls import path



urlpatterns = [
    path("", views.index, name="home"),
    path('cart/', views.view_cart, name='cart'),
    path('remove_from_cart/<int:order_product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path("product/<int:product_id>", views.product, name="product"),
    path("category/<int:category_id>", views.category, name="category"),
    path('wishlist/', views.view_wishlist, name='wishlist'),
    path('wishlist/remove/<int:wishlist_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
]