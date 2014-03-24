from natspec_utils.stringutils import stringToUnicode as u;

from cuescience_shop.tests.support.support import ClientTestSupport

from django.test.testcases import TestCase


class TestOrderNumberGeneration(TestCase):
    def setUp(self):
        self.client_test_support = ClientTestSupport(self)

    def test(self):
        """
         The code in this method is generated from: /de.iljabauer.projects.natspec.python/cuescience_shop/tests/models/test_order_number_generation.natspec
         Never change this method or any contents of this file, all local changes will we overwritten.
        """
        # Create address Test 11 01069 Dresden
        address_Test_11_01069_Dresden = self.client_test_support.create_address(u("Test"), u("11"), u("01069"), u("Dresden"))
        
        # Create client John Doe
        client_John_Doe = self.client_test_support.create_client(u("John"), u("Doe"), address_Test_11_01069_Dresden)
        
        # Create order
        order_ = self.client_test_support.create_order(client_John_Doe)
        
        # Assert order number is 0001
        self.client_test_support.assert_order_number(u("0001"), order_)
        
        