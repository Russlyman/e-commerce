from . import views
from django.urls import path



urlpatterns = [
    path("", views.index, name="home"),
    path('category/<int:category_id>/', views.item_category, name='item_category'),
    path('cart/', views.view_cart, name='cart'),
    path('remove_from_cart/<int:order_product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path("item/<int:product_id>", views.product, name="product"),
]