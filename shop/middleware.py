from django.http import HttpResponse
from .models import Order


class SetOrderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and "order" not in request.session:
            # Try and get an order for the user.
            order = Order.objects.filter(customer=request.user, order_date__isnull=True).first()

            # Create an order for the user if one doesn't exist already.
            if not order:
                order = Order.objects.create(customer=request.user)

            request.session["order"] = order.id

        response = self.get_response(request)
        return response
