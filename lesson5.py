# len_list = int(input('enter the length of the list: '))
# nums = []
# for i in range(len_list):
#     nums.append(int(input('enter the numbers: ')))
# nums.pop(int(input('enter the index to delete: ')))
# print(nums)

# len_list = int(input('enter the length of the list: '))
# nums = []
# for i in range(len_list):
#     nums.append(int(input('enter the numbers: ')))
# nums.remove(int(input('enter the number to delete: ')))
# nums.sort()
# print(nums[::-1])

# import random
# nums_range = list(range(1, 100))
# nums = random.sample(nums_range, 10)
# print(nums)
# max_num = max(nums)
# print(f'max is: {max_num}')
# nums.remove(max_num)
# nums.insert(0, max_num)
# print(nums)

import random
# nums = [random.randint(-10, 10) for i in range(10)]
# print(nums)
# neg = []
# for num in nums[::-1]:
#     if num < 0:
#         neg.append(num)
#         nums.remove(num)
# nums += neg
# print(nums)

# nums = [random.randint(-10, 10) for i in range(10)]
# print(nums)
# for i in range(len(nums) - 1, -1, -1):
#     if nums[i] < 0:
#         nums.append(nums.pop(i))
# print(nums)

# nums = [random.randint(1, 100) for i in range(10)]
# print(nums)
# index_minimal = nums.index(min(nums))
# nums = nums[index_minimal:]
# print(f'min: {min(nums)}')
# print(f'index min: {index_minimal}')
# print(nums)

# len_list1 = int(input('enter the length of the first list: '))
# len_list2 = int(input('enter the length of the second list: '))
# nums1 = [random.randint(1, 20) for i in range(len_list1)]
# nums2 = [random.randint(1, 20) for j in range(len_list2)]
# print(f'List1: {nums1}')
# print(f'List2: {nums2}')
# print(f'List3: {nums1+nums2}')
# print(f'Without repeating: {list(l for l in nums1 if l not in nums2) + list(l for l in nums2 if l not in nums1)}')
# print(f'Common elements: {list(k for k in nums1 if k in nums2)}')
# print(f'List3: {[min(nums1),max(nums1), min(nums2), max(nums2)]}')

len_list = int(input('enter the length of the list: '))
nums_range = list(range(0, 10))
nums = random.sample(nums_range, len_list)
print(nums)