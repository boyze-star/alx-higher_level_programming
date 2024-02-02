#!/usr/bin/python3
def add_integer(a, b = 98):
    """this function adds two int or float together"""
    if type(a) is not int and type(a) is not float:
        """checks if a is int or float"""
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        """checks if b is int or float"""
        raise TypeError("b must be an integer")
    if type(a) is None:
        raise ValueError("a is empty")
    if type(b) is None:
        raise ValueError("b is empty")

    if type(a) is float:
        a = int(a)
    """converts a to int if not"""
    if type(b) is float:
        b = int(b)
    """converts b to int if not"""

    return (a + b)

if __name__ == "__main__":
    """documentation included in add files and folders"""
    print(__import__("my_module").__doc__)
    print(__import__("my_module").add_integer.__doc__)
