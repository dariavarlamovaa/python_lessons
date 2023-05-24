# def sum_sum(a: int, b: int) -> int:
#     return a + b
#
#
# print(sum_sum(5, 9))


# def all_ops(a: int, b: int) -> tuple[int, int, int, float]:
#     return a + b, a - b, a * b, a / b
#
#
# sumsum, sub, mul, div = all_ops(3, 6)
# print(type(sumsum))


# import math
#
# print(int(math.sqrt(144)))

# import random
# # random.seed(1)
# print(random.randint(1, 5))
# print(random.random())
# print(random.choice([1, 5, 4, 9, 3, 4, 3]))
# print(random.sample([1, 5, 4, 9, 3, 4, 3], 3))


# import random
#
#
# def min_main(matrix):
#     # minimum = matrix[0][0]
#     # for i in range(len(matrix)):
#     #     if matrix[i][i] < minimum:
#     #         minimum = matrix[i][i]
#     # return minimum
#     return min([matrix[i][i] for i in range(len(matrix))])
#
#
#
# n = int(input('size: '))
# matrix = [[random.randint(1, 100)for i in range(n)] for j in range(n)]
# for row in matrix:
#     for num in row:
#         print(num, end='\t')
#     print()
#
# print(min_main(matrix))

# month = [[]]
# week = 0
# day = 1
# while day < 32:
#     if len(month[week]) < 7:
#         month[week].append(day)
#         day += 1
#     else:
#         week += 1
#         month.append([])
#
# [print(*row[:5], sep='\t') for row in month]
