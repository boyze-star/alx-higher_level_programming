#!/usr/bin/python3

def add_integer(a, b = 98):
    """
    Adds two integers.

    :param a: The first integer.
    :param b: The second integer (default is 98).
    :return: The sum of a and b as an integer.
    :raises TypeError: If a or b is not an integer or float.

    Examples:
    >>> add_integer(5, 3)
    8

    >>> add_integer(2.5, 3)
    5

    >>> add_integer("a", 3)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer or b must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)

if __name__ == "__main__":
    print(__import__("my_module").__doc__)
    print(__import__("my_module").add_integer.__doc__)
