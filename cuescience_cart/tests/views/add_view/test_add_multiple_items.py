from natspec_utils.stringutils import stringToUnicode as u;

from django.test.testcases import TestCase
from cuescience_cart.tests.support.support import TestSupport




class TestAddMultipleItems(TestCase):
    def setUp(self):
        self.test_support = TestSupport(self)

    def test(self):
        """
         The code in this method is generated from: /de.iljabauer.projects.natspec.python/cuescience_cart/tests/views/add_view/test_add_multiple_items.natspec
         Never change this method or any contents of this file, all local changes will we overwritten.
        """
        # Create product cuescience Scoreboard for 299.00
        self.test_support.create_product([u("cuescience"), u("Scoreboard")], 299.0)
        
        # Create product cuescience LiveCam for 150.00
        self.test_support.create_product([u("cuescience"), u("LiveCam")], 150.0)
        
        # Add cuescience Scoreboard to cart
        response_cuescience_Scoreboard = self.test_support.add_to_cart([u("cuescience"), u("Scoreboard")])
        
        # Assert status code: 302
        self.test_support.assert_status_code(302, response_cuescience_Scoreboard)
        
        # Add cuescience LiveCam to cart
        response_cuescience_LiveCam = self.test_support.add_to_cart([u("cuescience"), u("LiveCam")])
        
        # Assert status code: 302
        self.test_support.assert_status_code(302, response_cuescience_LiveCam)
        
        # Assert total cart item count: 2
        self.test_support.assert_total_item_count(2, response_cuescience_LiveCam)
        
        # Assert total cart price: 449.00
        self.test_support.assert_total_cart_price(449.0, response_cuescience_LiveCam)
        
        # Assert 1 cuescience Scoreboard in cart for 299.00
        __1_cuescience_Scoreboard_299_00 = self.test_support.assert_specific_item_in_cart(1, [u("cuescience"), u("Scoreboard")], 299.0, response_cuescience_LiveCam)
        
        # Assert 1 cuescience LiveCam in cart for 150.00
        __1_cuescience_LiveCam_150_00 = self.test_support.assert_specific_item_in_cart(1, [u("cuescience"), u("LiveCam")], 150.0, response_cuescience_LiveCam)
        
        