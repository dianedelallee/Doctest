import doctest


class MyClass:
    """MyClass
    >>> m = MyClass()
    >>> m.hello()
    hello
    >>> m.world()
    world
    """

    def hello(self):
        """method hello"""
        print('hello')

    def world(self):
        """method world"""
        print('world')


if __name__ == "__main__":
    doctest.testmod()
