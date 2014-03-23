""" @Imports """

from jinja2.environment import Environment
from jinja2.loaders import PackageLoader

from django_lean_modelling import helper
from django_lean_modelling.models.support import ModelSupport


class _NatSpecTemplate():
    
    model_support = ModelSupport()
    
    def generate_models(self):
        """ @MethodBody """
        

if __name__ == '__main__':
    model = _NatSpecTemplate()
    model.generate_models()

    env = Environment(loader=PackageLoader('cuescience_shop.specs', 'templates'), trim_blocks=False)
    template = env.get_template("model_template.py")
    
    content = template.render(models=model.model_support.models)
    
    f = open("../../%s.py" % helper.convert(model.__class__.__name__), 'w')
    f.write(content)
    f.close()