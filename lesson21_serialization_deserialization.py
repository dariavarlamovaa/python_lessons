# Сериализация - это способ преобразования структуры данных в линейную форму,
# которая может храниться или передаваться по сети.
# Десериализация - это процесс декодирования данных
# import json


# PICKLE
# import pickle
# string = 'Привет, мир'
# with open('file.txt', 'wb') as f:
#     pickle.dump(string, f)
#
# with open('file.txt', 'rb') as f:
#     text = pickle.load(f, encoding='ascii')
#     print(text)

# pickle.dumps()
# pickle.loads()

# import json


# class Shape:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def show(self):
#         info = ''
#         info += f'{self.__class__.__name__}:\n'
#         for key, value in self.__dict__.items():
#             info += f'\t{key}: {value}\n'
#         return info
#
#     def save(self, filename='file.txt'):
#         try:
#             Shape.load(filename)
#         except Exception:
#             open(filename, 'w')
#         with open(filename, 'a') as f:
#             f.write(f'{self.__class__.__name__}(**{self.__dict__})\n')
#
#     @staticmethod
#     def load(filename):
#         with open(filename, 'r') as f:
#             lines = f.readlines()
#             if len(lines) == 1:
#                 return eval(lines[0])
#             else:
#                 return list(map(eval, lines))
#
#     def __str__(self):
#         return self.show()
#
#
# class Circle(Shape):
#     def __init__(self, x, y, r):
#         Shape.__init__(self, x, y)
#         self.r = r
#
#
# class Rectangle(Shape):
#     def __init__(self, x, y, a, b):
#         Shape.__init__(self, x, y)
#         self.a = a
#         self.b = b
#
#
# class Square(Shape):
#     def __init__(self, x, y, a):
#         Shape.__init__(self, x, y)
#         self.a = a
#
#
# class Ellipse(Rectangle):
#     pass


# shapes = [Circle(10, 10, 5), Square(20, 20, 10),
#           Rectangle(30, 30, 5, 7), Ellipse(40, 40, 7, 5)]
#
# for shape in shapes:
#     shape.save('file.txt')
#
# new_shapes = Shape.load('file.txt')
# for shape in new_shapes:
#     print(shape)

# ---------------------------------------------

# JSON

# obj = Circle(2, 3, 4)
# json_string = {obj.__class__.__name__: obj.__dict__}
# with open('file.txt', 'w') as f:
#     json.dump(json_string, f)
# with open('file.txt', 'r') as f:
#     text = json.load(f)
#     new_obj = locals()[list(text.keys())[0]]
#     kwargs = list(text.values())[0]
#     print(new_obj(**kwargs))
# ---------------------------------------------

# circles = []
# for i in range(1, 10):
#     obj = Circle(i, 3, 5)
#     '''доделать'''
#     circles.append(f'{obj.__class__.__name__}(**{obj.__dict__})')
# with open('file.txt', 'w') as f:
#     json.dump(circles, f)
# with open('file.txt', 'r') as f:
#     text = json.load(f)
#     for obj in text:
#         print(eval(obj))

# ---------------------------------------------
# CSV

# import csv
#
# file = csv.reader(open('file.csv', 'r'))
# for i in file:
#     print(i)
#
# writer = csv.writer(open('file.csv', 'w'))
# writer.writerow([7,6,5,4])

# 1.
# def load():
#     with open('file.json', 'r') as f:
#         try:
#             content = json.load(f)
#             for key, value in content.items():
#                 print(f'{key}: {value}')
#         except FileExistsError:
#             content = {}
#         return content
#
#
# def save(content):
#     with open('file.json', 'w') as f:
#         json.dump(content, f)
#         print('the file has been updated')
#
#
# def add(content):
#     new_country = input('enter the name of the country: ').capitalize()
#     content[new_country] = input('enter its capital: ').capitalize()
#     print('the country has been added')
#
#
# def delete(content):
#     country_to_del = input('enter the name of the country to delete: ').capitalize()
#     del content[country_to_del]
#     print('the country has been deleted')
#
#
# def search(content):
#     country_to_search = input('enter the name of the country to find: ').capitalize()
#     if country_to_search in content:
#         print(country_to_search, content[country_to_search])
#     else:
#         print('country was not found')
#
#
# def replace(content):
#     country_to_replace = input('enter the name of the replace: ').capitalize()
#     content[country_to_replace] = input('enter its capital: ').capitalize()
#     print('the country has been replaced')
#
#
# def menu(content):
#     while True:
#         command = int(input('1-add, 2-del, \n'
#                             '3-find, 4-replace, \n'
#                             '5-save, 6-load, 0-exit \n'
#                             'enter the command: '))
#         if command == 1:
#             add(content)
#         elif command == 2:
#             delete(content)
#         elif command == 3:
#             search(content)
#         elif command == 4:
#             replace(content)
#         elif command == 5:
#             save(content)
#         elif command == 6:
#             load()
#         elif command == 0:
#             print('bye-bye')
#             break
#         else:
#             print('incorrect input. try again')
#             pass
#
#
# if __name__ == '__main__':
#     menu(load())
