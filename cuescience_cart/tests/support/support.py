from decimal import Decimal
from django.test import TestCase
from natspec_utils.decorators import TextSyntax
from cuescience_shop.models import Product
from django.test.client import Client
from cart.cart import Cart


class UpdateRequest(object):
    def __init__(self):
        self.data = {}

class TestSupport(object):
    def __init__(self, test_case):
        self.test_case = test_case
        self.client = Client()

    @TextSyntax("Create product #1 for #2", types=["list<str>", "float"])
    def create_product(self, title_words, price):
        title = " ".join(title_words)
        product = Product(title=title, price=price)
        product.save()

    @TextSyntax("Add #1 to cart", types=["list<str>", ], return_type="Response")
    def add_to_cart(self, title_words):
        title = " ".join(title_words)
        product = Product.objects.get(title=title)
        return self.add_product_to_cart(product.id)
    
    @TextSyntax("Add product #1 to cart", types=["int", ], return_type="Response")
    def add_product_to_cart(self, product_id):
        response = self.client.post("/cart/add/%s/" % product_id)
        return response
    
    @TextSyntax("Remove #1 from cart", types=["list<str>", ], return_type="Response")
    def remove_from_cart(self, title_words):
        title = " ".join(title_words)
        product = Product.objects.get(title=title)
        return self.remove_product_from_cart(product.id)

    @TextSyntax("Remove product #1 from cart", types=["int", ], return_type="Response")
    def remove_product_from_cart(self, product_id):
        response = self.client.post("/cart/remove/%s/" % product_id)
        return response

    @TextSyntax("Update cart:", return_type="UpdateRequest")
    def update_cart(self):
        return UpdateRequest()

    @TextSyntax("- #1 to quantity #2", types=["list<str>", "int", "UpdateRequest" ])
    def update_to_quantity(self, title_words, quantity, update_request):
        title = " ".join(title_words)
        product = Product.objects.get(title=title)
        update_request.data.update({"quantity-%s" % product.id: quantity})
        
    @TextSyntax("Send update", types=["UpdateRequest"], return_type="Response")
    def send_update(self, update_request):
        response = self.client.post("/cart/update/", update_request.data)
        return response

    @TextSyntax("Send get to #1", types=["str", ], return_type="Response")
    def send_get_to_url(self, url):
        response = self.client.get(url)
        return response

    @TextSyntax("Assert status code: #1", types=["int", "Response"])
    def assert_status_code(self, status_code, response):
        self.test_case.assertEqual(response.status_code, status_code)

    @TextSyntax("Assert total cart item count: #1", types=["int", "Response"])
    def assert_total_item_count(self, total_count, response):
        cart = Cart(self.client)
        count = cart.count()
        self.test_case.assertEqual(total_count, count)

    @TextSyntax("Assert total cart price: #1", types=["float", "Response"])
    def assert_total_cart_price(self, total_price, response):
        cart = Cart(self.client)
        price = cart.summary()
        self.test_case.assertEqual(total_price, price)

    @TextSyntax("Assert #1 #2 in cart for #3", types=["int", "list<str>", "float", "Response"])
    def assert_specific_item_in_cart(self, total_count, title_words, price, response):
        title = " ".join(title_words)
        product = Product.objects.get(title=title)
        cart = Cart(self.client)
        for item in cart:
            if product == item.product:
                self.test_case.assertEqual(total_count, item.quantity)
                self.test_case.assertEqual(price, item.total_price)
                return
        self.test_case.assertFalse(True, msg="Product not found: %s" % product.title)
        
    @TextSyntax("Assert #1 is not in cart", types=["list<str>", "Response"])
    def assert_specific_item_not_in_cart(self, title_words, response):
        title = " ".join(title_words)
        product = Product.objects.get(title=title)
        cart = Cart(self.client)
        for item in cart:
            self.test_case.assertFalse(product == item.product, msg="The %s product should not be in cart!" % title)
        
        
        
        
        
