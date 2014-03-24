from natspec_utils.stringutils import stringToUnicode as u;

from django.test.testcases import TestCase
from cuescience_cart.tests.support.support import TestSupport




class TestUpdateQuantityZero(TestCase):
    def setUp(self):
        self.test_support = TestSupport(self)

    def test(self):
        """
         The code in this method is generated from: /de.iljabauer.projects.natspec.python/cuescience_cart/tests/views/update_view/test_update_quantity_zero.natspec
         Never change this method or any contents of this file, all local changes will we overwritten.
        """
        # Create product cuescience Scoreboard for 299.00
        self.test_support.create_product([u("cuescience"), u("Scoreboard")], 299.0)
        
        # Add cuescience Scoreboard to cart
        response_cuescience_Scoreboard = self.test_support.add_to_cart([u("cuescience"), u("Scoreboard")])
        
        # Assert status code: 302
        self.test_support.assert_status_code(302, response_cuescience_Scoreboard)
        
        # Assert total cart item count: 1
        self.test_support.assert_total_item_count(1, response_cuescience_Scoreboard)
        
        # Assert total cart price: 299.00
        self.test_support.assert_total_cart_price(299.0, response_cuescience_Scoreboard)
        
        # Assert 1 cuescience Scoreboard in cart for 299.00
        __1_cuescience_Scoreboard_299_00 = self.test_support.assert_specific_item_in_cart(1, [u("cuescience"), u("Scoreboard")], 299.0, response_cuescience_Scoreboard)
        
        # Update cart:
        updateRequest_ = self.test_support.update_cart()
        
        # - cuescience Scoreboard to quantity 0
        self.test_support.update_to_quantity([u("cuescience"), u("Scoreboard")], 0, updateRequest_)
        
        # Send update
        response_ = self.test_support.send_update(updateRequest_)
        
        # Assert status code: 302
        self.test_support.assert_status_code(302, response_)
        
        # Assert total cart item count: 0
        self.test_support.assert_total_item_count(0, response_)
        
        # Assert total cart price: 0
        self.test_support.assert_total_cart_price(0.0, response_)
        
        # Assert cuescience Scoreboard is not in cart
        self.test_support.assert_specific_item_not_in_cart([u("cuescience"), u("Scoreboard")], response_)
        
        