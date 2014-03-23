""" @Imports """
from django.test.testcases import TestCase
from cuescience_cart.tests.support.test_support import TestSupport




class _NatSpecTemplate(TestCase):
    def setUp(self):
        self.test_support = TestSupport(self)

    def test(self):
        """ @MethodBody """