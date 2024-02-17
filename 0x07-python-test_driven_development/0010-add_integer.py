#!/usr/bin/python3
def add_integer(a, b=98):
    """checks if a is int or float"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or b must be an integr")
    """checks if b is int or float"""
    if not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    """cast a & b into int if float"""
    a = int(a)
    b = int(b)

    """returns addition of a & b"""
    return (a + b)
