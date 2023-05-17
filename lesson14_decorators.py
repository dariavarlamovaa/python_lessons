# Декораторы/decorators - функции, основной целью которых является
# изменение поведения других функций

# def check_positive(func):
#     def wrapper(a, b):
#         if func(a, b) < 0:
#             return 'error: sum is negative'
#         return func(a, b)
#
#     return wrapper
#
#
# @check_positive
# def summa(a, b):
#     return a + b
#
#
# print(summa(2,3))
# print(summa(2,-4))

# def prettify_output(func):
#     def wrapper(*args):
#         print('**********')
#         for i in range(5):
#             func(*args)
#         print('*********')
#
#     return wrapper
#
#
# @prettify_output
# def print_hello():
#     print('hello world!')
#
#
# print_hello()

# def summa(*args, **kwargs):
#     return sum(args) + sum(kwargs.values())
#
# print(summa(4,9,8,7))

# 1.
# def logging(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print(f'Function {func.__name__} was called with arguments: {*args, *kwargs} and returned {result}')
#         return result
#     return wrapper
#
# @logging
# def summa(a, b):
#     return a + b
#
# print(summa(2, 9))

# 2.
# def timer(func):
#     def wrapper(*args):
#         from time import time
#         start = time()
#         res = func(*args)
#         stop = time()
#         print('the result is', res)
#         print('finished in', stop - start, 'seconds')
#         return res
#     return wrapper
#
#
# @timer
# def summa(*args):
#     return sum(args)


# 3.
# def cache(func):
#     cache = {}
#
#     def wrapper(*args, **kwargs):
#         if (args, *kwargs.items()) not in cache:
#             cache[(args, *kwargs.items())] = func(*args, **kwargs)
#         return cache[(args, *kwargs.items())]
#
#     return wrapper
#
#
# @cache
# def slow_add(a, b, c):
#     print('loading...')
#     return a + b + c
#
#
# print(slow_add(3, 7, 4))
# print(slow_add(3, 7, 4))
# print(slow_add(5, 9, 4))
# print(slow_add(5, 9, 4))
# print(slow_add(a=1, b=2, c=3))
# print(slow_add(a=1, b=2, c=3))


# example
import random


def retry(num):
    def decorator(func):
        count = 0

        def wrapper(*args, **kwargs):
            nonlocal count
            while count < num:
                try:
                    return func(*args, **kwargs)
                except ValueError:
                    count += 1
                    print('function failed')
            raise Exception('too many calls!')

        return wrapper

    return decorator


@retry(3)
def random_func():
    if random.randint(0, 1):
        raise ValueError
    return 'function successfully executed'


print(random_func())
