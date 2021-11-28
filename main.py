from random import random


def simple_function_decorator(func):
    def wrapper(a, b):
        print("Hello from wrapper, you're launcing a function, called ", func.__name__, "().", sep="")
        return func(a, b)

    return wrapper


def iterable_decorator(iters):
    def actual_decorator(func):
        def wrapper(a, b):
            print("Hello from wrapper", iters, sep="")
            return func(a, b)

        return wrapper

    return actual_decorator


@iterable_decorator(iters=12)
def summ(a, b):
    return random()

print(summ(12, 23))
