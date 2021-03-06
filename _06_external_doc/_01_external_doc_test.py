import doctest

__test__ = {
    'numbers_from_file_1':"""
>>> my_function(2, 3)
6

>>> my_function(2.0, 3)
6.0
""",

    'strings':"""
>>> my_function('a', 3)
'aaa'

>>> my_function(3, 'a')
'aaa'
""",
    }

def my_function(a, b):
    """Returns a * b
    """
    return a * b

if __name__ == "__main__":
    doctest.testmod()
