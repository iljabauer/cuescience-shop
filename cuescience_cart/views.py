from cart import Cart
from cuescience_shop.models import Product
from django.http import Http404, HttpResponseNotAllowed
from django.shortcuts import redirect


def add_view(request, product_id, next="/"):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    cart = Cart(request)
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404

    cart.add(product, product.price)

    return redirect(next)


def remove_view(request, product_id, next="/"):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    cart = Cart(request)
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404

    cart.remove(product)

    return redirect(next)