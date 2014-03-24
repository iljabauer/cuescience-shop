from decimal import Decimal
from django.test import TestCase
from natspec_utils.decorators import TextSyntax
from cuescience_shop.models import Product
from django.test.client import Client
from cart.cart import Cart


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
        self.add_product_to_cart(product.id)
    
    @TextSyntax("Add product #1 to cart", types=["int", ], return_type="Response")
    def add_product_to_cart(self, product_id):
        response = self.client.post("/cart/add/%s/" % product_id)
        return response
    
    @TextSyntax("Remove #1 from cart", types=["list<str>", ], return_type="Response")
    def remove_from_cart(self, title_words):
        title = " ".join(title_words)
        product = Product.objects.get(title=title)
        response = self.client.post("/cart/remove/%s/" % product.id)
        return response

    @TextSyntax("Assert status code: #1", types=["int", "Response"])
    def assert_status_code(self, status_code, response):
        self.test_case.assertEqual(response.status_code, status_code)

    @TextSyntax("Assert total cart item count: #1", types=["int", "Response"])
    def assert_total_item_count(self, total_count, response):
        cart = Cart(self.client)
        count = 0
        for item in cart:
            count += item.quantity
        self.test_case.assertEqual(total_count, count)

    @TextSyntax("Assert total cart price: #1", types=["float", "Response"])
    def assert_total_cart_price(self, total_price, response):
        cart = Cart(self.client)
        price = Decimal(0.0)
        for item in cart:
            price += item.total_price
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
        
        
        
        
        