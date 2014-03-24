from cart import Cart
from cuescience_shop.checkout_wizard import CheckoutWizardBase, condition_step_3
from cuescience_shop.models import Product, Order
from django.shortcuts import render_to_response
from django.template import RequestContext


def index_view(request):
    products = Product.objects.all()
    return render_to_response("cuescience_shop/index.html", RequestContext(request, {"products": products}))


class CheckoutWizard(CheckoutWizardBase):
    template_name = "cuescience_shop/wizard.html"

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

        return render_to_response("cuescience_shop/index.html", RequestContext(self.request))
