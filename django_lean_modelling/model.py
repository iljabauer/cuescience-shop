class Commentable():
    pass

class Clazz(object):
    def __init__(self, name):
        self.name = name
        self.properties = []
        self.comment = ""
        
class Model(Clazz, Commentable):
    def __init__(self, name, verbose_name, verbose_name_plural = None):
        super(Model, self).__init__(name)
        self.verbose_name = verbose_name
        if not verbose_name_plural:
            verbose_name_plural = verbose_name+"s"
        self.verbose_name_plural = verbose_name_plural
        
class Admin(Clazz):
    def __init__(self, model):
        name = model.name + "Admin"
        super(Admin, self).__init__(name)
        self.model = model

    
class Property(object, Commentable):
    def __init__(self, name, definition):
        self.name = name
        self.definition = definition
        self.args = []
        self.kwargs = {}
        self.comment = ""