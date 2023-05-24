# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
#
# while num1 <= num2:
#     if num1 % 2 != 0:
#         print(num1)
#     num1 += 1
#
# start, end = int(input('Введите первое число: ')), int(input('Введите второе число: '))
# while start != end:
#     print(end)
#     end -= 1
#
# start, end = int(input('Введите первое число: ')), int(input('Введите второе число: '))
# if start > end:
#     start, end = end, start
# while start <= end:
#     if start % 2 != 0:
#         print(start)
#     start += 1
#
# start = int(input('1: '))
# stop = int(input('2: '))
# q = 0
# su = 0
# for i in range(start, stop):
#     q += 1
#     su = su + q
# print(su/q)
#
# first, second = input('Введите первое число: '), input('Введите второе число: ')
# try:
#     print(int(first) + int(second))
# except ValueError:
#     print(str(first) + str(second))
#
# a = input()
# b = input()
# try:
#     a = int(a)
#     b = int(b)
#     print(a+b)
# except ValueError:
#     a = str(a)
#     print(a+b)
#
# a = int(input('Введите длину строки:'))
# b = input('Введите символ:')
# while a > 0:
#     print(b, end='')
#     a -= 1
#
# total = 1
# while True:
#     number = int(input('Введите значение: '))
#     if number == 0:
#         break
#     total *= number
# print(total)
#
# for i in range(1, 10):
#     for r in range(1, 10):
#         print(f"{i}*{r}={i*r}", end='\t')
#     print()

# length = int(input('Введите длину: '))
# height = int(input('Введите высоту: '))
# char = input('Введите символ: ')
# for j in range(height):
#     for i in range(length):
#         print(char, end='')
#     print()

# num1 = int(input('введите начало: '))
# num2 = int(input('введите конец: '))
# while True:
#     num3 = int(input('введите число: '))
#     if num1 <= num3 <= num2:
#         print('Число не в диапазоне')
#         break
# for i in range(num1, num2 + 1):
#     if i == num3:
#         i = f'!{i}!'
#     print(i, end=' ')

# number = int(input('Введите целое число: '))
# number_list = []
# for i in range(1, number//2 + 1):
#     if not number % i:
#         number_list.append(i)
#         print(*number_list)

# import random
# import time
# number = random.randint(1, 500)
# print(number)
# start = time.time()
# count = 0
# while True:
#     num1 = int(input("Угадайте число в диапазоне от 1 до 500: "))
#     count += 1
#     if num1 == 0:
#         print("Конец игры!")
#         break
#     elif num1 == number:
#         print("Угадали!")
#         print("Затраченное время:", time.time() - start)
#         print("Попыток: ", count)
#         break
#     else:
#         print("Не верно! Попробуйте еще раз")
#         if num1 > number:
#             print("Загаданное число меньше")
#         else:
#             print("Загаданное число больше")

# for i in range(5):
#     print(i*" "+"*")


row = int(input('number:'))
string = ''
for i in range(1, row + 1):
    string += str(i)
    print(string)
