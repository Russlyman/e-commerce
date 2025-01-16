from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="home"),
    path('category/<int:category_id>/', views.item_category, name='item_category'),
    path("item/<int:product_id>", views.product, name="product"),
]