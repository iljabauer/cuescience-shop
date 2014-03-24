from natspec_utils.stringutils import stringToUnicode as u;

from django.test.testcases import TestCase
from cuescience_cart.test.support.test_support import TestSupport




class AddMultipleItemsTest(TestCase):
    def setUp(self):
        self.test_support = TestSupport(self)

    def test(self):
        """
         The code in this method is generated from: /de.iljabauer.projects.natspec.python/cuescience_cart/test/add_multiple_items_test.natspec
         Never change this method or any contents of this file, all local changes will we overwritten.
        """
        # Create product cuescience Scoreboard for 299.00
        self.test_support.create_product([u("cuescience"), u("Scoreboard")], 299.0)
        
        # Create product cuescience LiveCam for 150.00
        self.test_support.create_product([u("cuescience"), u("LiveCam")], 150.0)
        
        # Add cuescience Scoreboard to cart
        self.test_support.add_to_cart([u("cuescience"), u("Scoreboard")])
        
        # Add cuescience LiveCam to cart
        self.test_support.add_to_cart([u("cuescience"), u("LiveCam")])
        
        