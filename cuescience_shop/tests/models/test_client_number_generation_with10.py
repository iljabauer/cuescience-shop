from natspec_utils.stringutils import stringToUnicode as u;

from cuescience_shop.tests.support.support import ClientTestSupport

from django.test.testcases import TestCase


class TestClientNumberGenerationWith10(TestCase):
    def setUp(self):
        self.client_test_support = ClientTestSupport(self)

    def test(self):
        """
         The code in this method is generated from: /de.iljabauer.projects.natspec.python/cuescience_shop/tests/models/test_client_number_generation_with_10.natspec
         Never change this method or any contents of this file, all local changes will we overwritten.
        """
        # Create address Test 11 01069 Dresden
        address_Test_11_01069_Dresden = self.client_test_support.create_address(u("Test"), u("11"), u("01069"), u("Dresden"))
        
        # Create client Client One
        client_Client_One = self.client_test_support.create_client(u("Client"), u("One"), address_Test_11_01069_Dresden)
        
        # Create address Test 11 01069 Dresden
        address_Test_11_01069_Dresden0 = self.client_test_support.create_address(u("Test"), u("11"), u("01069"), u("Dresden"))
        
        # Create client Client Two
        client_Client_Two = self.client_test_support.create_client(u("Client"), u("Two"), address_Test_11_01069_Dresden0)
        
        # Create address Test 11 01069 Dresden
        address_Test_11_01069_Dresden1 = self.client_test_support.create_address(u("Test"), u("11"), u("01069"), u("Dresden"))
        
        # Create client Client Three
        client_Client_Three = self.client_test_support.create_client(u("Client"), u("Three"), address_Test_11_01069_Dresden1)
        
        # Create address Test 11 01069 Dresden
        address_Test_11_01069_Dresden2 = self.client_test_support.create_address(u("Test"), u("11"), u("01069"), u("Dresden"))
        
        # Create client Client Four
        client_Client_Four = self.client_test_support.create_client(u("Client"), u("Four"), address_Test_11_01069_Dresden2)
        
        # Create address Test 11 01069 Dresden
        address_Test_11_01069_Dresden3 = self.client_test_support.create_address(u("Test"), u("11"), u("01069"), u("Dresden"))
        
        # Create client Client Five
        client_Client_Five = self.client_test_support.create_client(u("Client"), u("Five"), address_Test_11_01069_Dresden3)
        
        # Create address Test 11 01069 Dresden
        address_Test_11_01069_Dresden4 = self.client_test_support.create_address(u("Test"), u("11"), u("01069"), u("Dresden"))
        
        # Create client Client Six
        client_Client_Six = self.client_test_support.create_client(u("Client"), u("Six"), address_Test_11_01069_Dresden4)
        
        # Create address Test 11 01069 Dresden
        address_Test_11_01069_Dresden5 = self.client_test_support.create_address(u("Test"), u("11"), u("01069"), u("Dresden"))
        
        # Create client Client Seven
        client_Client_Seven = self.client_test_support.create_client(u("Client"), u("Seven"), address_Test_11_01069_Dresden5)
        
        # Create address Test 11 01069 Dresden
        address_Test_11_01069_Dresden6 = self.client_test_support.create_address(u("Test"), u("11"), u("01069"), u("Dresden"))
        
        # Create client Client Eight
        client_Client_Eight = self.client_test_support.create_client(u("Client"), u("Eight"), address_Test_11_01069_Dresden6)
        
        # Create address Test 11 01069 Dresden
        address_Test_11_01069_Dresden7 = self.client_test_support.create_address(u("Test"), u("11"), u("01069"), u("Dresden"))
        
        # Create client Client Nine
        client_Client_Nine = self.client_test_support.create_client(u("Client"), u("Nine"), address_Test_11_01069_Dresden7)
        
        # Create address Test 11 01069 Dresden
        address_Test_11_01069_Dresden8 = self.client_test_support.create_address(u("Test"), u("11"), u("01069"), u("Dresden"))
        
        # Create client Client Ten
        client_Client_Ten = self.client_test_support.create_client(u("Client"), u("Ten"), address_Test_11_01069_Dresden8)
        
        # Assert client number is 0010
        self.client_test_support.assert_client_number(u("0010"), client_Client_Ten)
        
        