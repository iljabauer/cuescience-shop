from natspec_utils.stringutils import stringToUnicode as u;

from django.test.testcases import TestCase
from cuescience_cart.tests.support.support import TestSupport




class TestUpdateQuantity(TestCase):
    def setUp(self):
        self.test_support = TestSupport(self)

    def test(self):
        """
         The code in this method is generated from: /de.iljabauer.projects.natspec.python/cuescience_cart/tests/views/update_view/test_update_quantity.natspec
         Never change this method or any contents of this file, all local changes will we overwritten.
        """
        # Create product cuescience Scoreboard for 300.00
        self.test_support.create_product([u("cuescience"), u("Scoreboard")], 300.0)
        
        # Create product cuescience LiveCam for 150.00
        self.test_support.create_product([u("cuescience"), u("LiveCam")], 150.0)
        
        # Add cuescience Scoreboard to cart
        response_cuescience_Scoreboard = self.test_support.add_to_cart([u("cuescience"), u("Scoreboard")])
        
        # Add cuescience LiveCam to cart
        response_cuescience_LiveCam = self.test_support.add_to_cart([u("cuescience"), u("LiveCam")])
        
        # Assert status code: 302
        self.test_support.assert_status_code(302, response_cuescience_LiveCam)
        
        # Assert total cart item count: 2
        self.test_support.assert_total_item_count(2, response_cuescience_LiveCam)
        
        # Assert total cart price: 450.00
        self.test_support.assert_total_cart_price(450.0, response_cuescience_LiveCam)
        
        # Assert 1 cuescience Scoreboard in cart for 300.00
        __1_cuescience_Scoreboard_300_00 = self.test_support.assert_specific_item_in_cart(1, [u("cuescience"), u("Scoreboard")], 300.0, response_cuescience_LiveCam)
        
        # Assert 1 cuescience LiveCam in cart for 150.00
        __1_cuescience_LiveCam_150_00 = self.test_support.assert_specific_item_in_cart(1, [u("cuescience"), u("LiveCam")], 150.0, response_cuescience_LiveCam)
        
        # Update cart:
        updateRequest_ = self.test_support.update_cart()
        
        # - cuescience Scoreboard to quantity 4
        self.test_support.update_to_quantity([u("cuescience"), u("Scoreboard")], 4, updateRequest_)
        
        # Send update
        response_ = self.test_support.send_update(updateRequest_)
        
        # Assert status code: 302
        self.test_support.assert_status_code(302, response_)
        
        # Assert total cart item count: 5
        self.test_support.assert_total_item_count(5, response_)
        
        # Assert total cart price: 1350.00
        self.test_support.assert_total_cart_price(1350.0, response_)
        
        # Assert 4 cuescience Scoreboard in cart for 1200.00
        __4_cuescience_Scoreboard_1200_00 = self.test_support.assert_specific_item_in_cart(4, [u("cuescience"), u("Scoreboard")], 1200.0, response_)
        
        # Update cart:
        updateRequest_0 = self.test_support.update_cart()
        
        # - cuescience LiveCam to quantity 2
        self.test_support.update_to_quantity([u("cuescience"), u("LiveCam")], 2, updateRequest_0)
        
        # Send update
        response_0 = self.test_support.send_update(updateRequest_0)
        
        # Assert status code: 302
        self.test_support.assert_status_code(302, response_0)
        
        # Assert total cart item count: 6
        self.test_support.assert_total_item_count(6, response_0)
        
        # Assert total cart price: 1500.00
        self.test_support.assert_total_cart_price(1500.0, response_0)
        
        # Assert 2 cuescience LiveCam in cart for 300.00
        __2_cuescience_LiveCam_300_00 = self.test_support.assert_specific_item_in_cart(2, [u("cuescience"), u("LiveCam")], 300.0, response_0)
        
        