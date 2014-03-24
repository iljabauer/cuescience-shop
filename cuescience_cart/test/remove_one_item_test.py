from natspec_utils.stringutils import stringToUnicode as u;

from django.test.testcases import TestCase
from cuescience_cart.test.support.test_support import TestSupport




class RemoveOneItemTest(TestCase):
    def setUp(self):
        self.test_support = TestSupport(self)

    def test(self):
        """
         The code in this method is generated from: /de.iljabauer.projects.natspec.python/cuescience_cart/test/remove_one_item_test.natspec
         Never change this method or any contents of this file, all local changes will we overwritten.
        """
        # Create product cuescience Scoreboard for 299.00
        self.test_support.create_product([u("cuescience"), u("Scoreboard")], 299.0)
        
        # Add cuescience Scoreboard to cart
        self.test_support.add_to_cart([u("cuescience"), u("Scoreboard")])
        
        # Remove cuescience Scoreboard from cart
        response_cuescience_Scoreboard = self.test_support.remove_from_cart([u("cuescience"), u("Scoreboard")])
        
        # Assert total cart item count: 0
        self.test_support.assert_total_item_count(0, response_cuescience_Scoreboard)
        
        # Assert total cart price: 0
        self.test_support.assert_total_cart_price(0.0, response_cuescience_Scoreboard)
        
        