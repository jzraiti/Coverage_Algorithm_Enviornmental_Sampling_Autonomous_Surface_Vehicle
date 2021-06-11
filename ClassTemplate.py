class Template(object):

    def __init__(self):
        self.value = "hello"
        self.other_value = "bonjour"
        self.constant_value = 42
        current_class = self.__class__
        inits = []
        while (current_class.__name__ != "Template"):
            inits.append(current_class.init)
            current_class = current_class.__bases__[0]
        for i in reversed(inits):
            i(self)

    def init(self):
        pass

    def info(self):
        print (self.value)
        print (self.other_value)
        print (self.constant_value)
        print ("")

class Deep(Template):
    def init(self):
        self.value = "howdy"
        self.other_value = "salut"

class Deeep(Deep):
    def init(self):
        self.value = "hi"

class Deeeep(Deeep):
    def init(self):
        self.value = "'sup"

very_deep = Deeeep()
not_so_deep = Deep()
very_deep.info()
not_so_deep.info()