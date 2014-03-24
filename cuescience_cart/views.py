from cart import Cart
from cuescience_shop.models import Product
from django.http import Http404, HttpResponseNotAllowed
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext


def index_view(request):
    return render_to_response("cuescience_cart/index.html", RequestContext(request))


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


def update_view(request, next="/"):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    cart = Cart(request)
    for item in cart:
        quantity = request.POST.get("quantity-%s" % item.id, None)
        isNone = quantity is None
        isSame = int(quantity) == item.quantity
        if isNone or isSame:
            return redirect(next)

        quantity = int(quantity)
        if quantity == 0:
            item.delete()
            return redirect(next)

        item.quantity = quantity
        item.save()

    return redirect(next)