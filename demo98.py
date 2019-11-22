import doctest

def square(x):
    """ return sss of x.
    >>> square(4)
    16
    >>> square(2)
    4
    :param x:
    :return:
    """

    return x**x
if __name__ =='__main__':
    doctest.testmod()
