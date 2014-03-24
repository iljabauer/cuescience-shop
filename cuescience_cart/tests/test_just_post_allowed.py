from natspec_utils.stringutils import stringToUnicode as u;

from django.test.testcases import TestCase
from cuescience_cart.tests.support.support import TestSupport




class TestJustPostAllowed(TestCase):
    def setUp(self):
        self.test_support = TestSupport(self)

    def test(self):
        """
         The code in this method is generated from: /de.iljabauer.projects.natspec.python/cuescience_cart/tests/test_just_post_allowed.natspec
         Never change this method or any contents of this file, all local changes will we overwritten.
        """
        # Send get to /cart/add/1/
        response__cart_add_1_ = self.test_support.send_get_to_url(u("/cart/add/1/"))
        
        # Assert status code: 405
        self.test_support.assert_status_code(405, response__cart_add_1_)
        
        # Send get to /cart/remove/1/
        response__cart_remove_1_ = self.test_support.send_get_to_url(u("/cart/remove/1/"))
        
        # Assert status code: 405
        self.test_support.assert_status_code(405, response__cart_remove_1_)
        
        