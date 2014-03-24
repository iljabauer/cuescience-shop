""" @Imports """
from django.test.testcases import TestCase
from cuescience_cart.tests.support.support import TestSupport




class TestRemoveNonExistingProduct(TestCase):
    def setUp(self):
        self.test_support = TestSupport(self)

    def test(self):
        """
         The code in this method is generated from: /de.iljabauer.projects.natspec.python/cuescience_cart/tests/views/remove_view/test_remove_non_existing_product.natspec
         Never change this method or any contents of this file, all local changes will we overwritten.
        """
        # Remove product 1 from cart
        response_1 = self.test_support.remove_product_from_cart(1)
        
        # Assert status code: 404
        self.test_support.assert_status_code(404, response_1)
        
        # Assert total cart item count: 0
        self.test_support.assert_total_item_count(0, response_1)
        
        # Assert total cart price: 0
        self.test_support.assert_total_cart_price(0.0, response_1)
        
        