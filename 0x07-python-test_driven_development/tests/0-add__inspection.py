#!/usr/bin/python3
    """
    Check if a function takes zero arguments.

    :param func: The function to check.
    :return: True if the function takes zero arguments, False otherwise.
    """
    def has_zero_args(func):
        return all(param.default == param.empty for param in parameters.values())
    if not func:
        raise ValueError("no args passed to function")
    print(has_zero_args(zero_args_function))  # Output: True
    print(has_zero_args(one_arg_function))    # Output: False
