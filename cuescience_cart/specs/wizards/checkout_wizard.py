from natspec_utils.stringutils import stringToUnicode as u;


from django_lean_modelling import helper
from django_lean_modelling.forms.wizard_suport import WizardSupport

from jinja2.environment import Environment
from jinja2.loaders import PackageLoader


class CheckoutWizard():
    
    wizard_support = WizardSupport()
    
    
    def generate_models(self):
        """
         The code in this method is generated from: /de.iljabauer.projects.natspec.python/cuescience_cart/specs/wizards/checkout_wizard.natspec
         Never change this method or any contents of this file, all local changes will we overwritten.
        """
        # Checkout wizard:
        wizard_Checkout = self.wizard_support.create_wizard([u("Checkout")])
        
        # Step 1:
        step_1 = self.wizard_support.step_definition(1, wizard_Checkout)
        
        # Form based on Client model:
        modelForm_Client = self.wizard_support.modelform_definition([u("Client")], step_1)
        
        # - first_name.
        self.wizard_support.form_modelfield_definition([u("first_name")], modelForm_Client)
        
        # - last_name.
        self.wizard_support.form_modelfield_definition([u("last_name")], modelForm_Client)
        
        # Step 2:
        step_2 = self.wizard_support.step_definition(2, wizard_Checkout)
        
        # Form based on Address model:
        modelForm_Address = self.wizard_support.modelform_definition([u("Address")], step_2)
        
        # Heading: Shipping Address
        self.wizard_support.heading_definition([u("Shipping"), u("Address")], modelForm_Address)
        
        # - street | number.
        self.wizard_support.form_modelfield_definition([u("street"), u("|"), u("number")], modelForm_Address)
        
        # - postcode | city.
        self.wizard_support.form_modelfield_definition([u("postcode"), u("|"), u("city")], modelForm_Address)
        
        # - Different billing address? (different billing address) - Checkbox.
        __Different_billing_address__different_billing_address_Checkbox = self.wizard_support.form_field_definition([u("Different"), u("billing"), u("address?")], [u("different"), u("billing"), u("address")], u("Checkbox"), modelForm_Address)
        
        # Step 3:
        step_3 = self.wizard_support.step_definition(3, wizard_Checkout)
        
        # Condition: different billing address from step 2 is True
        self.wizard_support.condition_definition([u("different"), u("billing"), u("address")], 2, [u("True")], step_3)
        
        # Form based on Address model:
        modelForm_Address0 = self.wizard_support.modelform_definition([u("Address")], step_3)
        
        # Heading: Billing Address
        self.wizard_support.heading_definition([u("Billing"), u("Address")], modelForm_Address0)
        
        # - street | number.
        self.wizard_support.form_modelfield_definition([u("street"), u("|"), u("number")], modelForm_Address0)
        
        # - postcode | city.
        self.wizard_support.form_modelfield_definition([u("postcode"), u("|"), u("city")], modelForm_Address0)
        
        # Step 4:
        step_4 = self.wizard_support.step_definition(4, wizard_Checkout)
        
        # Form:
        modelForm_ = self.wizard_support.form_definition(step_4)
        
        # Heading: Payment options
        self.wizard_support.heading_definition([u("Payment"), u("options")], modelForm_)
        
        # - Please choose one (paypent options) - Choices are Prepayment PayPal.
        self.wizard_support.form_field_choices_definition([u("Please"), u("choose"), u("one")], [u("paypent"), u("options")], [u("Prepayment"), u("PayPal")], modelForm_)
        
        
        

if __name__ == '__main__':
    model = CheckoutWizard()
    model.generate_models()

    env = Environment(loader=PackageLoader('cuescience_cart.specs', 'templates'), trim_blocks=False)
    template = env.get_template("wizard_template.py")
    content = template.render(wizard=model.wizard_support.wizard)

    
    f = open("../../%s.py" % helper.convert(model.__class__.__name__), 'w')
    f.write(content)
    f.close()