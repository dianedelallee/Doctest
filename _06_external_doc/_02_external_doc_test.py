import doctest
import external_doc_test

__test__ = {
    'numbers':"""
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

'external':external_doc_test,

    }

def my_function(a, b):
    """Returns a * b
    """
    return a * b

if __name__ == "__main__":
    doctest.testmod()
