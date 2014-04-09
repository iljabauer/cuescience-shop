from cart import Cart
from cuescience_cart.checkout_wizard import CheckoutWizardBase, condition_step_3
from cuescience_shop.models import Product, Order
from django.http import Http404, HttpResponseNotAllowed
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext


def index_view(request):
    return render_to_response("cuescience_cart/index.html", RequestContext(request))


def add_view(request, product_id):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    next = request.GET.get("next", "/")

    cart = Cart(request)
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404

    cart.add(product, product.price)

    return redirect(next)


def remove_view(request, product_id):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    next = request.GET.get("next", "/")

    cart = Cart(request)
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404

    cart.remove(product)

    return redirect(next)


def update_view(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    next = request.GET.get("next", "/")

    cart = Cart(request)
    for item in cart:
        quantity = request.POST.get("quantity-{0}".format(item.product.pk), None)
        isNone = quantity is None
        
        if isNone:
            continue
        isSame = int(quantity) == item.quantity
        if isSame:
            continue

        quantity = int(quantity)
        if quantity == 0:
            item.delete()
            return redirect(next)

        item.quantity = quantity
        item.save()

    return redirect(next)


class CheckoutWizard(CheckoutWizardBase):
    template_name = "cuescience_cart/wizard.html"

    def done(self, form_list, **kwargs):
        cart = Cart(self.request)
        order = Order(cart=cart.cart)

        client = form_list[0].save(commit=False)
        address = form_list[1].save()
        client.shipping_address = address
        billing_address = address
        if condition_step_3(self):
            billing_address = form_list[2].save()
        client.billing_address = billing_address
        client.save()

        order.client = client
        order.save()

        # we need to do the checkout as last operation,
        # if something went wrong
        cart.check_out()

        return render_to_response("cuescience_cart/index.html", RequestContext(self.request))