#!/usr/bin/python3
def add_integer(a, b = 98):
    """this function adds two int or float together"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)

if __name__ == "__main__":
    print(__import__("my_module").__doc__)
    print(__import__("my_module").add_integer.__doc__)
