# Линейный поиск
# nums = [1,2,3,4]
# for i in nums:
#     if i == 3:
#         print(i)
#         break


# Бинарный(двоичный поиск)
# def binary_search(nums, key):
#     start, end = 0, len(nums)
#     count = 0
#     while start <= end:
#         count += 1
#         current = (end + start) // 2
#         if nums[current] == key:
#             return nums[current], count
#         elif nums[current] < key:
#             start = current + 1
#         else:
#             end = current - 1
#     return 'there is no number'
#
#
# nums = [i for i in range(100)]
# print(binary_search(nums, 5))

# 1.
# import random
#
#
# def binary_search(nums, key):
#     start, end = 0, len(nums)
#     while start <= end:
#         current = (end + start) // 2
#         if nums[current] == key:
#             return 'number {} is in the {} position'.format(key, current)
#         elif nums[current] < key:
#             start = current + 1
#         else:
#             end = current - 1
#     return 'there is no {}'.format(key)
#
#
# user_nums = [random.randint(1, 30) for _ in range(10)]
# user_nums.sort()
# print(user_nums)
#
# print(binary_search(user_nums, int(input('enter the number: '))))

# Сортировка Шелла
# import math


# def shell_sort(nums):
#     count = 0
#     k = int(math.log2(len(nums)))
#     interval = 2 ** k - 1
#     while interval > 0:
#         for i in range(interval, len(nums)):
#             key = nums[i]
#             j = i
#             while j >= interval and nums[j - interval] > key:
#                 nums[j] = nums[j - interval]
#                 j -= interval
#             nums[j] = key
#         count +=1
#         k -= 1
#         interval = 2 ** k - 1
#     return nums, count
#
#
# print(shell_sort([1, 6, 2, 7, 5, 9]))

# OR


# def shell_sort(nums):
#     count = 0
#     interval = len(nums) // 2
#     while interval > 0:
#         for i in range(interval, len(nums)):
#             key = nums[i]
#             j = i
#             while j >= interval and nums[j - interval] > key:
#                 nums[j] = nums[j - interval]
#                 j -= interval
#             nums[j] = key
#         count += 1
#         interval //= 2
#     return nums, count
#
#
# print(shell_sort([1, 6, 2, 7, 5, 9]))

# Алгоритм быстрой сортировки
# def quick_sort(nums):
#     if len(nums) <= 1:
#         return nums
#     pivot = nums.pop()
#     left, mid, right = [], [pivot], []
#     for num in nums:
#         if num < pivot:
#             left.append(num)
#         elif num > pivot:
#             right.append(num)
#         else:
#             mid.append(num)
#     return quick_sort(left) + mid + quick_sort(right)
#
# print(quick_sort([4,2,6,1,7]))

# 1.
# def pancakes_sort(pancakes):
#     length = len(pancakes)
#     count = 0
#     for i in range(length):
#         m = max(pancakes[:length])
#         m_index = pancakes.index(m)
#         pancakes[m_index:length] = reversed(pancakes[m_index:length])
#         length -= 1
#         count +=1
#         print(pancakes)
#     return pancakes[::-1], count
#
#
# nums = [5, 6, 8, 6, 12, 10, 9, 13]
#
# print(pancakes_sort(nums))
