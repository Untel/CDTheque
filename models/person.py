class Person:
    
    def __init__(self, name):
        self._name = name

    def _get_name(self):
        return self._name
    def _set_name(self, name):
        self._name = name.upper()
    name = property(_get_name, _set_name)

    
# class Interpreter(Person):
#     def __init(self):

# class Author(Person):
#     def __init(self):

# class Composer(Person):