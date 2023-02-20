# matrix
# import random
# n = int(input('width: '))
# m = int(input('length: '))
# matrix = [[random.randint(1, 9) for i in range(n)]for j in range(m)]
# for row in matrix:
#     for num in row:
#         print(num, end='\t')
#     print()

# heights = ['167', '155', '123', '144']
# for i in range(len(heights)):
#     heights[i] = int(heights[i])

# heights = list(map(int, heights))
# print(heights)

# n = int(input('width: '))
# m = int(input('length: '))

# matrix = [[i + n * j + 1 for i in range(n)] for j in range(m)]
# print(matrix)

# 1
# matrix = []
# n = int(input('Введите ширину матрицы: '))
# m = int(input('Введите высоту матрицы: '))

# matrix = [[i + n * j + 1 for i in range(n)] for j in range(m)]
#  ^^^ Генерация матрицы в одну строку через генераторы ^^^

# value = 1
# for i in range(m):
#     row = []
#     for j in range(n):
#         row.append(value)
#         print(value, end='\t')
#         value += 1
#     print()
#     matrix.append(row)
# print('\t' * m)
# for i in range(m):
#     for j in range(n):
#         matrix[i][j] **= 2
#         print(matrix[i][j], end='\t')
#     print()

# 2.
# matrix = [[0 for i in range(10)] for j in range(10)]
# for i in range(10):
#     matrix[i][i] = 1
#     if i < len(matrix[0]) - 1:
#         matrix[i][i + 1] = 1
#     if i > 0:
#         matrix[i][i - 1] = 1
#
# for row in matrix:
#     for num in row:
#         print(num, end='\t')
#     print()

# 3.
# import random
# n, m = 5, 5
# matrix = [[random.randint(1, 20) for i in range(n)] for j in range(m)]
#
# for row in matrix:
#     for num in row:
#         print(num, end='\t')
#     print()
#
# maximum = matrix[0][0]
# for row in matrix:
#     maximum = max(maximum, max(row))
#
# Альтернативный способ нахождения максимума
# one_line = []
# for row in matrix:
#     one_line.extend(row)
# maximum = max(one_line)
#
# columns = []
# for i in range(m):
#     for j in range(n):
#         if matrix[i][j] == maximum:
#             if j not in columns:
#                 columns.append(j)
# print('------------------')
# for i in range(m):
#     for col in columns:
#         print(matrix[i][col], end='\t')
#     print()

# 4.
# import random
#
# n, m = 3, 2
# matrix = [[random.randint(1, 20) for i in range(n)] for j in range(m)]
#
# for row in matrix:
#     for num in row:
#         print(num, end='\t')
#     print()
#
# lucky_nums = []
# for i in range(m):
#     for j in range(n):
#         num = matrix[i][j]
#         minimum = num == min(matrix[i])
#         maximum = True
#         for k in range(m):
#             if num < matrix[k][j]:
#                 maximum = False
#         if minimum and maximum:
#             lucky_nums.append(num)
#
# print(lucky_nums)
