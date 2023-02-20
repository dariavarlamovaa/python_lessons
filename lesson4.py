# lll = []
# for i in range(10):
#     lll.append(int(input('enter the number: ')))
# target = int(input('what number to find: '))
# count = 0
# for num in lll:
#     if num == target:
#         count += 1
# print(f'the number was found {count} times')

# nums = [1,2,3,4,5,6,7]
# print(nums)
# print(nums[::-1])
# print(nums[::2])
# print(nums[1:7:2])
# print(nums[0:1])
# print(nums[-1:])
# print(nums[3:4])
# print(nums[4:7])
# print(nums[-3:1:-1])
# print(nums[2:5])

# numbers_list = []
# for i in range(10):
#     numbers_list.append(int(input('enter the number: ')))
# print(sum(numbers_list))
# print(sum(numbers_list)/len(numbers_list))

# llll = []
# for i in range(1,11):
#     llll.extend([i**2])
# print(llll)

# numbers = []
# length = int(input('enter the length: '))
#
# for i in range(length):
#     num = int(input('enter the number:'))
#     if num % 3 == 0:
#         numbers.append(num)
#     else:
#         print('this number is not a multiple of 3')
# print(numbers)

# numbers = [x**2 for x in range(1, 11)]
# print(numbers)

num1 = [1, 2, 3]
num2 = [11, 22, 33]
nums = []
for i in range(len(num1)):
    nums.append(num1[i])
    nums.append(num2[i])
print(nums)