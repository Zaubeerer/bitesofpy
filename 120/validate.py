from functools import wraps


def int_args(func):
    @wraps(func)
    # complete this decorator