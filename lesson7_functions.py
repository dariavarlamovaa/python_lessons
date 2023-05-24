# homework
# people = ['Daria', 'Lera', 'Sasha', 'Vera', 'Lara']
# heights = [175, 180, 187, 160, 169]
# # el and index
# data = [[heights[i], i] for i in range(5)]
# data.sort(reverse=True)
# sorted_people = [people[value[1]] for value in data]
# print(sorted_people)

# homework2
# import random
# nums = [random.randint(1, 10) for i in range(5)]
# print(nums)
# new_nums = [sum(i < j for i in nums) for j in nums]
# print(new_nums)

# functions
# def hello_world():
#     print('hello world!')
#
#
# hello_world()

# arguments
# def sum_sum(a, b):
#     return a + b
#
#
# res = sum_sum(4, 5)
# print(res)

# default arguments
# def multiply(a, b=4):
#     return a * b
#
#
# print(multiply(4, 5))
# print(multiply(4))

# lucky nums
# def is_lucky(n):
#     n = str(n)
#     print(n)
#     return int(n[0]) + int(n[1]) + int(n[2]) == \
#         int(n[3]) + int(n[4]) + int(n[5])
#
# print(is_lucky(555555))

import random
#
#
# def sort_matrix(matrix):
#     # for i in range(len(matrix)):
#     #     if i % 2 == 0:
#     #         matrix[i].sort(reverse=True)
#     #     else:
#     #         matrix[i].sort()
#     # return matrix
#     return [matrix[i].sort(reverse=i % 2 == 0) for i in range(len(matrix))]
#
#
# n, m = int(input('width: ')), int(input('length: '))
# main_matrix = [[random.randint(1, 15) for i in range(n)]for j in range(m)]
# for row in main_matrix:
#     for num in row:
#         print(num, end='\t')
#     print()
#
# print('_________________')
# sort_matrix(main_matrix)
# for row in main_matrix:
#     for num in row:
#         print(num, end='\t')
#     print()


def multiply_indexes(matrix):
    main_matrix = [[random.randint(0, 4) for i in range(3)]
                   for j in range(5)]
    res = 1
    for i in matrix:
        for el in i:
            res = res * el if el > 0 else res
            print(el, end='\t')
        print()
    return res


multiply_indexes()
