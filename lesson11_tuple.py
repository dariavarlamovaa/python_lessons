# TUPLE
# 1.
# my_tuple = ('apple', 'banana', 'mango', 'apple', 'mango')
# print(input(my_tuple.count(input('enter the fruit: '))))
#
# # 2.
# my_tuple = ('apple', 'bananamango', 'mango', 'apple-banana', 'mango')
# fruit = input('enter the fruit: ')
# counter = 0
# for i in my_tuple:
#     if fruit in i:
#         counter += 1
# print(counter)

# 3.
# cars = ('bmw', 'mercedes', 'lada', 'lada', 'bmw', 'tesla', 'lexus')
# print(str(cars).replace(input('enter the car brand: ').lower(),
#                         input('enter the new word: ')))
# # OR
# target, replacement = input('enter the car brand: ').lower(), input('enter the new word: ')
# print(tuple(replacement if brand == target else brand for brand in cars))
#

# SET
# my_set = {1, 2, 3, 4, 5, 6, 7, 3}
# print(my_set)

# vasya_books = {'Idiot', 'Lady', 'Don'}
# nadya_books = {'Idiot', 'It', 'The Ring'}
# print(vasya_books.union(nadya_books))
# print(vasya_books.difference(nadya_books))
# print(vasya_books.intersection(nadya_books))
# print(vasya_books.pop())
# numbers = {1, 2, 3, 4, 5}
# numbers.discard(5)
# print(numbers)
# numbers.add(9)
# print(numbers)
# numbers.update((2, 5, 6, 3))
# print(numbers)

# countries = {'Russia', 'Finland', 'Latvia', 'Ukraine', 'Uranus'}
#
#
# def func():
#     while True:
#         command = int(input('enter the command (1-add, 2-del, 3-find, 4-check): '))
#         if command > 4 or command <= 0:
#             print('incorrect input. try again')
#             pass
#         if command == 1:
#             countries.add(input('enter the new country: '))
#             print(countries)
#         if command == 2:
#             countries.discard(input('enter the county to delete: '))
#             print(countries)
#         if command == 3:
#             find = input('enter the symbols: ').lower()
#             print(tuple(country for country in countries if country.lower().startswith(find)))
#         if command == 4:
#             con = input('enter the country to check: ')
#             print(countries.isdisjoint(con))
#
#
# func()


