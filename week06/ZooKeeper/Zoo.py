from animal import Animal, Cat

class Zoo(object):
    """
    class Zoo
    """
    def __init__(self, name):
        self.name = name

    def add_animal(self, animal : Animal):
        setattr(self, animal.__class__.__name__, animal)

if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', 'predacity', 'small', 'tender', True)
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')

    print (have_cat)
    print (z.Cat)