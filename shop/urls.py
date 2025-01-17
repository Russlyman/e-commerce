from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="home"),
    path("product/<int:product_id>", views.product, name="product"),
    path("category/<int:category_id>", views.category, name="category"),
]