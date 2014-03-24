from natspec_utils.stringutils import stringToUnicode as u;

from django.test.testcases import TestCase
from cuescience_cart.tests.support.support import TestSupport




class TestCheckoutWizard(TestCase):
    def setUp(self):
        self.test_support = TestSupport(self)

    def test(self):
        """
         The code in this method is generated from: /de.iljabauer.projects.natspec.python/cuescience_cart/tests/views/checkout_wizard/test_checkout_wizard.natspec
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
        
        # Select cart
        cart_ = self.test_support.select_cart()
        
        # Checkout cart
        response_ = self.test_support.checkout_cart()
        
        # Assert step 1 of wizard is displayed
        self.test_support.assert_step_of_wizard(1, response_)
        
        # Enter data:
        checkoutRequest_ = self.test_support.submit_data()
        
        # - current step: 1
        currentStep_1 = self.test_support.current_step_data(1, checkoutRequest_)
        
        # - first name: John
        self.test_support.collect_checkout_data([u("first"), u("name")], [u("John")], checkoutRequest_, currentStep_1)
        
        # - last name: Doe
        self.test_support.collect_checkout_data([u("last"), u("name")], [u("Doe")], checkoutRequest_, currentStep_1)
        
        # Submit
        response_0 = self.test_support.submit(checkoutRequest_)
        
        # Assert step 2 of wizard is displayed
        self.test_support.assert_step_of_wizard(2, response_0)
        
        # Enter data:
        checkoutRequest_0 = self.test_support.submit_data()
        
        # - current step: 2
        currentStep_2 = self.test_support.current_step_data(2, checkoutRequest_0)
        
        # - street: Test Street
        self.test_support.collect_checkout_data([u("street")], [u("Test"), u("Street")], checkoutRequest_0, currentStep_2)
        
        # - number: 11
        self.test_support.collect_checkout_data([u("number")], [u("11")], checkoutRequest_0, currentStep_2)
        
        # - postcode: 01069
        self.test_support.collect_checkout_data([u("postcode")], [u("01069")], checkoutRequest_0, currentStep_2)
        
        # - city: Dresden
        self.test_support.collect_checkout_data([u("city")], [u("Dresden")], checkoutRequest_0, currentStep_2)
        
        # - different billing address: False
        self.test_support.collect_checkout_data([u("different"), u("billing"), u("address")], [u("False")], checkoutRequest_0, currentStep_2)
        
        # Submit
        response_1 = self.test_support.submit(checkoutRequest_0)
        
        # Assert step 4 of wizard is displayed
        self.test_support.assert_step_of_wizard(4, response_1)
        
        # Enter data:
        checkoutRequest_1 = self.test_support.submit_data()
        
        # - current step: 4
        currentStep_4 = self.test_support.current_step_data(4, checkoutRequest_1)
        
        # - paypent_options: PayPal
        self.test_support.collect_checkout_data([u("paypent_options")], [u("PayPal")], checkoutRequest_1, currentStep_4)
        
        # Submit
        response_2 = self.test_support.submit(checkoutRequest_1)
        
        # Assert total cart item count: 0
        self.test_support.assert_total_item_count(0, response_2)
        
        # Select client: John, Doe
        client_John_Doe = self.test_support.select_client([u("John")], [u("Doe")])
        
        # Assert client has shipping address: Test Street, 11, 01069, Dresden
        self.test_support.assert_client_shipping_address([u("Test"), u("Street")], [u("11")], u("01069"), [u("Dresden")], u("shipping"), client_John_Doe)
        
        # Assert client has billing address: Test Street, 11, 01069, Dresden
        self.test_support.assert_client_shipping_address([u("Test"), u("Street")], [u("11")], u("01069"), [u("Dresden")], u("billing"), client_John_Doe)
        
        # Assert order with cart exists
        order_ = self.test_support.assert_order_with_cart_exists(cart_)
        
        # Assert order has abovementioned client
        self.test_support.assert_order_has_client(order_, client_John_Doe)
        
        