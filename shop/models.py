from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = CloudinaryField("image", default="placeholder")

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    name = models.CharField(max_length=50)
    SKU = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100)
    image = CloudinaryField("image", default="placeholder")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name


class Wishlist(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="wishlist"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="in_wishlist"
    )

    def __str__(self):
        return f"{self.customer.username} - {self.product.name}"


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    order_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Order {self.id} - {self.customer.username}"


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="products")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="orders"
    )
    quantity = models.IntegerField()

    def __str__(self):
        return f"Order {self.order.id} - {self.order.customer.username} - {self.product.name}"


# class Rating(models.Model):
#     """
#     Represents a rating for a product. Users can rate a recipe and optionally leave a review.
#     Each rating is linked to a specific product and a user.
#     """

#     product = models.ForeignKey(
#         Product, on_delete=models.CASCADE, related_name="ratings"
#     )
#     customer = models.ForeignKey(User, on_delete=models.CASCADE)
#     rating = models.IntegerField()
#     review = models.TextField(max_length=500, blank=True)
#     created_at = models.DateTimeField(
#         auto_now_add=True, help_text="The date and time the rating was created."
#     )

#     class Meta:

#         unique_together = ["product", "customer"]
