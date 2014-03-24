""" @Imports """

from jinja2.environment import Environment
from jinja2.loaders import PackageLoader

from django_lean_modelling import helper
from django_lean_modelling.models.support import ModelSupport
from django_lean_modelling.admin.support import AdminSupport


class Models():
    
    model_support = ModelSupport()
    admin_support = AdminSupport()
    
    def generate_models(self):
        """
         The code in this method is generated from: /de.iljabauer.projects.natspec.python/cuescience_shop/specs/models/models.natspec
         Never change this method or any contents of this file, all local changes will we overwritten.
        """
        
        

if __name__ == '__main__':
    model = Models()
    model.generate_models()

    env = Environment(loader=PackageLoader('cuescience_shop.specs', 'templates'), trim_blocks=False)
    template = env.get_template("model_template.py")
    
    content = template.render(models=model.model_support.models)
    
    template_admin = env.get_template("admin_template.py")
    content_admin = template_admin.render(admins=model.admin_support.admins)
    
    f = open("../../%s.py" % helper.convert(model.__class__.__name__), 'w')
    f.write(content)
    f.close()
    f1 = open("../../admin.py", 'w')
    f1.write(content_admin)
    f1.close()