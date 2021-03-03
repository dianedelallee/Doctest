import doctest

def this_raises():
    """This function always raises an exception.

    >>> this_raises()
    Traceback (most recent call last):
    ...
    RuntimeError: here is the errorpipen
    """
    raise RuntimeError('here is the error')


if __name__ == "__main__":
    doctest.testmod()
