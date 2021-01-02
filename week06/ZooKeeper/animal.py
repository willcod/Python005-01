from Singleton import Singleton

class Animal(object):
    """
    Base class of all kinds of animals
    """
    
    def __init__(self, typeof, size:int, character):
        if type(self) == Animal:
            raise Exception("Class Animal can't be initiated")
        self.typeof = typeof
        self.size = size
        self.character = character
    
    @property
    def IsFierce(self):
        return (self.size == 'middle' or self.size == 'large') \
            and self.character == 'fierce' \
            and self.typeof == 'predacity'


class Cat(Animal, metaclass=Singleton):
    """
    class Cat
    """
    sound = 'miao'

    def __init__(self, name, typeof, size:int, character, pet:bool):
        self.name = name
        self.pet = pet
        Animal.__init__(self, typeof, size, character)


class Dog(Animal, metaclass=Singleton):
    """
    class Dog
    """
    sound = 'oh'

    def __init__(self, name, typeof, size:int, character):
        self.name = name
        Animal.__init__(self, typeof, size, character)
        

if __name__ == '__main__':
    cat = Cat('Big Cat One', 'predacity', 'small', 'tender', True)
    print (cat.IsFierce)
    print (cat.sound)
    cat2 = Cat('Big Cat Two', 'predacity', 'small', 'tender', True)

    print (cat.name == cat2.name)
