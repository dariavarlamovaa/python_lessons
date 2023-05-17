# bubble sort

# nums = [8, 7, 4, 2, 9, 3, 1, 5]
# for _ in range(len(nums)):
#     for j in range(len(nums) - 1):
#         if nums[j] > nums[j + 1]:
#             nums[j], nums[j + 1] = nums[j + 1], nums[j]
# print(nums)

# or

# nums = [8, 7, 4, 2, 9]
# swapped = True
# while swapped:
#     swapped = False
#     for j in range(len(nums) - 1):
#         if nums[j] > nums[j+1]:
#             nums[j], nums[j+1] = nums[j+1], nums[j]
#             print(nums)
#             swapped = True
# print(nums)

# selection sort

# nums = [7, 4, 8, 5, 2, 1]
#
#
# def selection_sort(nums):
#     for i in range(len(nums)):
#         lowest = i
#         for j in range(i + 1, len(nums)):
#             if nums[j] < nums[lowest]:
#                 lowest = j
#         nums[i], nums[lowest] = nums[lowest], nums[i]
#     return nums
#
#
# print(selection_sort(nums))


# insertion sort

# nums = [6, 5, 4, 2, 3]
# for k in range(1, len(nums)):
#     cur = nums[k]
#     j = k
#     while nums[j-1] > cur and j > 0:
#         nums[j] = nums[j-1]
#         j -= 1
#     nums[j] = cur
#     print(nums)
# print(nums)


# merge sort

# def merge_sort(spisok):
#     if len(spisok) <= 1:
#         return spisok
#     L = merge_sort(spisok[:len(spisok) // 2])
#     R = merge_sort(spisok[len(spisok) // 2:])
#     n = m = k = 0
#     C = [0] * (len(L) + len(R))
#
#     while n < len(L) and m < len(R):
#         if L[n] <= R[m]:
#             C[k] = L[n]
#             n += 1
#         else:
#             C[k] = R[m]
#             m += 1
#         k += 1
#
#     while n < len(L):
#         C[k] = L[n]
#         n += 1
#         k += 1
#
#     while m < len(R):
#         C[k] = R[m]
#         m += 1
#         k += 1
#
#     return C
#
# print(merge_sort([9,8,4,6,2,7]))

# 1.
# nums = [4,4,9,7,3,5,9,2]
# mid = len(nums)//2
# left = nums[:mid]
# right = nums[mid:]
# for l in range(1, len(left)):
#     cur = left[l]
#     j = l
#     while left[j-1] < cur and j > 0:
#         left[j] = left[j-1]
#         j -= 1
#     left[j] = cur
# for r in range(1, len(right)):
#     cur = right[r]
#     j = r
#     while right[j - 1] > cur and j > 0:
#         right[j] = right[j - 1]
#         j -= 1
#     right[j] = cur
# nums = left+right
# print(nums)
