# def print_symbols(a: int = 20, b: str = '-'):
#     print(b * a)
#
#
# print_symbols()
# print_symbols(8)
# print_symbols(9, '%')


# def count_odd_and_even_numbers(num: int, even: bool = True):
#     list_nums = list(map(int, list(str(num))))
#     return sum([i for i in list_nums if i % 2 != even])
#
#
# evens = 'не'
# print(f'Сумма {evens}четных: {count_odd_and_even_numbers(111222, bool(not evens))}')


# recursive functions

# def fibo(n: int):
#     if n == 1:
#         return 0
#     elif n == 2 or n == 3:
#         return 1
#     else:
#         return fibo(n - 1) + fibo(n - 2)
#
#
# print(fibo(40))


# def r(n: int):
#     print(n)
#     if n == 0:
#         return
#     r(n-1)
#     print(n)
#
#
# r(2)

# def draw_symbols(length: int = 10, symbol: str = '-'):
#     if length > 0:
#         print(symbol, end='')
#         length -= 1
#         draw_symbols(length, symbol)
#
#
# draw_symbols()


# def count_exp(number: int, deg: int) -> int:
#     return number * count_exp(number, deg - 1) if deg != 0 else 1
#
#
# print(count_exp(8, 0))
# print(count_exp(4, 3))

# def summ(a, b):
#     return a + summ(a + 1, b) if a < b else b
#
#
# print(summ(3, 5))
# import random
#
#
# def find_index(nums=None, i=0, final_sum=0, index=0):
#     if nums is None:
#         nums = [random.randint(1, 100) for i in range(1, 30)]
#     cur_min = sum([nums[i] for i in range(i, i + 10)])
#     if final_sum > cur_min or final_sum == 0:
#         final_sum = cur_min
#         index = 1
#     try:
#         return find_index(nums, i + 1, final_sum == 0)
#     except IndexError:
#         for i in range(len(nums)):
#             if index <= i < index + 10:
#                 print('\033[32m', end='')
#             else:
#                 print('\033[0m', end='')
#                 print(nums[i], end=' ')
#         print()
#         return final_sum, index
#
#
# print(find_index())
