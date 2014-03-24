""" @Imports """
from django.test.testcases import TestCase
from cuescience_cart.tests.support.support import TestSupport




class TestAddNonExistingProduct(TestCase):
    def setUp(self):
        self.test_support = TestSupport(self)

    def test(self):
        """
         The code in this method is generated from: /de.iljabauer.projects.natspec.python/cuescience_cart/tests/test_add_non_existing_product.natspec
         Never change this method or any contents of this file, all local changes will we overwritten.
        """
        # Add product 1 to cart
        response_1 = self.test_support.add_product_to_cart(1)
        
        # Assert status code: 404
        self.test_support.assert_status_code(404, response_1)
        
        # Assert total cart item count: 0
        self.test_support.assert_total_item_count(0, response_1)
        
        # Assert total cart price: 0
        self.test_support.assert_total_cart_price(0.0, response_1)
        
        