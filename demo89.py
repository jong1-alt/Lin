class MetaSingleton(type):
    _instances= {}
    def __call__(self, *args, **kwargs):
        print('insid ......')
        if self not in self._instances:
            print("object not yet created")
            print("create one")
            self._instances[self] = \
                super().__call__(*args, **kwargs)
        print('return insta')
        return self._instances[self]

    pass

class SingletonClass(metaclass=MetaSingleton):
    def __init__(self):
        print(f'sc id={hex(id(self))}')
x1 = Singletonclass()
x2 = Singletonclass()
print(x1 == x2, hex(id(x1), hex(id(x2)))