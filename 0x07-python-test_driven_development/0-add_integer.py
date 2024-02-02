#!/usr/bin/python3
def add_integer(a, b = 98):
    """this function adds two int or float together"""
    if not isinstance(a, (int, float)):
        """checks if a is int or float"""
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        """checks if b is int or float"""
        raise TypeError("b must be an integer")

    a = int(a)
    """converts a to int if not"""
    b = int(b)
    """converts b to int if not"""

    return (a + b)

if __name__ == "__main__":
    """documentation included in att files and folders"""
    print(__import__("my_module").__doc__)
    print(__import__("my_module").add_integer.__doc__)
