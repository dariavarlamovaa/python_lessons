# Именование классов подчиняется принципу CamelCase
# class Glass:
#     def __init__(self, volume):
#         self.volume = volume
#         self.filling = None
#
#     def fill_up(self, liquid):
#         self.filling = liquid
#
#
# a = Glass(0.5)
# print(a.volume)
# a.fill_up('Water')
# print(a.filling)
# import math
# a.new = 123
# print(a.new)

# del a.new
# print(a.new)


# 1.
# class Human:
#     def __init__(self, fullname, birthday, telephone, city, country, address):
#         self.fullname = fullname
#         self.birthday = birthday
#         self.telephone = telephone
#         self.city = city
#         self.country = country
#         self.address = address
#
#     def fill_it_up(self):
#         self.fullname = input('enter your full name: ')
#         self.birthday = input('enter your birthday: ')
#         self.telephone = input('enter your telephone: ')
#         self.city = input('enter your city: ')
#         self.country = input('enter your country: ')
#         self.address = input('enter your address: ')
#
#     def print_info(self):
#         print(self.fullname, self.birthday, self.telephone,
#               self.city, self.country, self.address, sep='\n')
#
#
# person = Human('Ivan Ivanov', '01.01.2001', '89123123123', 'Petrozavodsk', 'Russia', 'Lenina pr. 1-101')
# person.fill_it_up()
# person.print_info()


# Наследование
# class Number:
#     def __init__(self, num):
#         self.num = num
#
#     def square(self):
#         return int(self.num) ** 2
#
#
# class Float(Number):
#     def square(self):
#         return self.num ** 2
#
#
# a = Number(5)
# print(a.square())
# b = Float(6.6)
# print(b.square())

# 2.
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def square(self):
#         return self.length * self.width
#
#     def perimeter(self):
#         return 2 * (self.length + self.width)
#
#
# r = Rectangle(10, 5)
# print(r.square())
# print(r.perimeter())

# ----------------------------------------------------------

# ДЕКОРАТОРЫ В КЛАССАХ
# import math


#
#
# class Number:
#     def __init__(self, num):
#         self.num = num
#
#     # @staticmethod
#     def square_root(self):
#         return math.sqrt(self.num)
#
#     @classmethod
#     def print_name(cls):
#         print(cls.__name__)
#
#
# a = Number(5)
# print(a.square_root())
# Number.print_name()

# class Person:
#     @staticmethod
#     def is_adult(age):
#         if age > 18:
#             return True
#         return False
#
# print(Person.is_adult(44))


# 3.
# class Human:
#     count = 0
#
#     def __init__(self):
#         self.fullname = ''
#         self.birthday = ''
#         self.telephone = ''
#         self.city = ''
#         self.country = ''
#         self.address = ''
#         self.__class__.count += 1
#
#     def fill_it_up(self):
#         self.fullname = input('enter your full name: ')
#         self.birthday = input('enter your birthday: ')
#         self.telephone = input('enter your telephone: ')
#         self.city = input('enter your city: ')
#         self.country = input('enter your country: ')
#         self.address = input('enter your address: ')
#
#     def print_info(self):
#         print(self.fullname, self.birthday, self.telephone,
#               self.city, self.country, self.address, sep='\n')
#
#     @staticmethod
#     def print_count():
#         print(Human.count)
#
#
# person = Human()
# person.fill_it_up()
# person.print_info()
# Human.print_count()
# person2 = Human()
# person2.fill_it_up()
# person2.print_info()
# Human.print_count()


# 4.
# import math
#
#
# class Square:
#     count = 0
#
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def triangle_square(side1, side2, side3):
#         Square.count += 1
#         p = (side1 + side2 + side3) / 2
#         st1 = math.sqrt(p * (p - side1) * (p - side2) * (p - side3))
#         return st1
#
#     @staticmethod
#     def triangle_square2(side1, height):
#         Square.count += 1
#         st2 = (side1 * height) / 2
#         return st2
#
#     @staticmethod
#     def rectangle_square(side1, side2):
#         Square.count += 1
#         sr = side1 * side2
#         return sr
#
#     @staticmethod
#     def area_square(side1):
#         Square.count += 1
#         ss = side1 ** 2
#         return ss
#
#     @staticmethod
#     def rhombus_square(d1, d2):
#         Square.count += 1
#         roms = (d1 * d2) / 2
#         return roms
#
#     @staticmethod
#     def counter():
#         print(f'counter = {Square.count}')
#
#
# area = Square()
# print(area.triangle_square2(10, 3))
# print(area.triangle_square(10, 10, 10))
# Square.counter()


# другие декораторы
# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#
#     @property
#     def age(self):
#         print('you are reaching sensitive attribute')
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         self.__age = value
#
#     @age.deleter
#     def age(self):
#         raise Exception('Нельзя удалить!!!')
#
#
# a = Human('Ivan', 20)
# print(a.name)
# print(a.age)
# a.age = 5
# print(a.age)
# del a.age


# class Circle:
#     def __init__(self, r):
#         self.r = r
#
#     @property
#     def area(self):
#         return self.r ** 2
#
#
# a = Circle(5)
# print(a.r)
# print(a.area)
# a.r = 6
# print(a.area)


# 5.
# class Shape:
#     def __init__(self, name):
#         self.name = name
#
#     def print_info(self):
#         print(f'{self.name}')
#         if hasattr(self, 'area'):
#             print(f'Square: {self.area}')
#
#
# class Circle(Shape):
#     def __init__(self, r):
#         Shape.__init__(self, 'Окружность')
#         self.r = r
#
#     @property
#     def circle_square(self):
#         return self.r ** 2 * 3.14
#
#
# class Square(Shape):
#     def __init__(self, side1):
#         Shape.__init__(self, 'Квадрат')
#         self.side1 = side1
#
#     @property
#     def area_square(self):
#         return self.side1 ** 2
#
#
# e = Shape('Фигура')
# print(e.name)
# a = Circle(5)
# b = Square(3)
# print(a.name)
# print(a.circle_square)
# print(b.name)
# print(b.area_square)


# ----------------------------------------------------------
# АБСТРАКТНЫЕ КЛАССЫ
# from abc import ABC, abstractmethod
#
# class A(ABC):
#     """Базовый абстрактный класс"""
#
#     def __init__(self, size):
#         self.size = size
#
#     @abstractmethod
#     def get_size(self):
#         pass
#
#
# class B(A):
#     def __init__(self, size):
#         A.__init__(self, size)
#         self.other = 5
#
#     def get_size(self):
#         return self.size
#
#
# b = B(6)
# print(b.size)
# print(b.get_size())


# 1.
# class Human(ABC):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_info(self):
#         return f'This is {self.name}. He is {self.age}.' \
#                f' He works as a {self.occupation}'
#
#     @abstractmethod
#     def occupation(self):
#         pass
#
#
# class Builder(Human):
#     @property
#     def occupation(self):
#         return 'Builder'
#
#
# class Sailor(Human):
#     @property
#     def occupation(self):
#         return 'Sailor'
#
#
# class Pilot(Human):
#     @property
#     def occupation(self):
#         return 'Pilot'
#
#
# h1 = Builder('Ivan', 23)
# print(h1.get_info())


# ---------------------
# class Time:
#     def __init__(self, hours, mins, secs):
#         self.hours = hours
#         self.mins = mins
#         self.secs = secs
#
#     def __add__(self, other):
#         return Time(self.hours + other.hours, self.mins + other.mins,
#                     self.secs + other.secs)
#
#
# a = Time(12, 0, 0)
# b = Time(14, 30, 0)
# c = a + b
# print(c.hours, c.mins)

# ------------

# class Float:
#     def __init__(self, numerator, denominator):
#         self.numerator = numerator
#         self.denominator = denominator
#
#     def __add__(self, other):
#         return Float(self.numerator * other.denominator + other.numenator * self.denominator,
#                      self.denominator * other.denominator)
#
#     def __radd__(self, other):
#         return self.__add__(other)
#
#
# a = Float(2, 3)
# b = Float(1, 2)
# c = 5 + a
# print(c.numerator, c.denominator)

# 1.
# class Number:
#     def __init__(self, num):
#         self.num = num
#
#     def __add__(self, other):
#         return Number(self.num + other.num)
#
#     def __sub__(self, other):
#         return Number(self.num - other.num)
#
#     def __mul__(self, other):
#         return Number(self.num * other.num)
#
#     def __truediv__(self, other):
#         return Number(self.num / other.num)
#
#
# a = Number(50)
# b = Number(3)
# c = a * b
# print(c.num)

# ----------------
# class Float:
#     def __init__(self, num, denom):
#         self.numerator = num
#         self.denominator = denom

# def __repr__(self):
#     return f'{self.numerator}/{self.denominator}'
#

#     def __eq__(self, other):
#         return self.numerator / self.denominator == \
#             other.numeraotr / other.demonimator
#
#     def __ne__(self, other):
#         pass
#
#     def __gt__(self, other):
#         pass
#
#     def __ge__(self, other):
#         pass
#
#     def __lt__(self, other):
#         pass
#
#     def __str__(self):
#         return f'{self.numerator}/{self.denominator}'
#
#
# a = Float(4, 5)
# print(a != 0.5)
# print(a)


# 2.
# class Library:
#     def __init__(self, name, address, number_of_books):
#         self.name = name
#         self.address = address
#         self.number_of_books = number_of_books
#
#     def __add__(self, other):
#         self.number_of_books = self.number_of_books + other
#         return self.number_of_books
#
#     def __sub__(self, other):
#         self.number_of_books = self.number_of_books - other
#         return self.number_of_books
#
#     def __iadd__(self, other):
#         self.number_of_books += other
#         return self
#
#     def __isub__(self, other):
#         self.number_of_books -= other
#         return self
#
#     def __lt__(self, other):
#         return self.number_of_books < other.number_of_books
#
#     def __gt__(self, other):
#         return self.number_of_books > other.number_of_books
#
#     def __le__(self, other):
#         return self.number_of_books <= other.number_of_books
#
#     def __ge__(self, other):
#         return self.number_of_books >= other.number_of_books
#
#     def __eq__(self, other):
#         return self.number_of_books == other.number_of_books
#
#     def __ne__(self, other):
#         return self.number_of_books != other.number_of_books
#
#
# a = Library('Main', 'Lenina street 1', 349055)
# b = Library('Small', 'Lenina street 78', 90333)
# a + 10
# b += 100
# print(a.number_of_books)
# print(b.number_of_books)
# print(a > b)

# ----------------------------------------------------------
# МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ
# class A:
#     def __init__(self):
#         self.a = 3
#
#     def print_a_value(self):
#         print(self.a)
#
#
# class B:
#     def __init__(self):
#         self.b = 5
#
#
# class C(A, B):
#     def print_b_value(self):
#         print(self.b)
#
# a = C()
# a.print_b_value() # ошибка, тк в классе А нет такого метода

# 1.
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     @property
#     def area(self):
#         return 3.14 * (self.radius ** 2)
#
#
# class Square:
#     def __init__(self, length):
#         self.length = length
#
#     @property
#     def area(self):
#         return self.length ** 2
#
#
# class CS(Circle, Square):
#     def __init__(self, circle, square):
#         circle.__class__.__init__(self, circle.passengers)  # same as Circle.__init__(self, circle.radius)
#         square.__class__.__init__(self, square.length)  # same as Square.__init__(self, circle.length)
#         if self.radius * 2 > self.length:
#             raise ValueError('error!')
#         self.circle = circle
#         self.square = square
#
#     @property
#     def area(self):
#         return self.square.area - self.circle.area
#
#
# a = Circle(5)
# b = Square(10)
# print(a.area)
# print(b.area)
# c = CS(a, b)
# print(c.area)

# 2.
# class Wheels:
#     def __init__(self, wheels):
#         self.wheels = wheels
#
#
# class Engine:
#     def __init__(self, engine):
#         self.engine = engine
#
#
# class Body:
#     def __init__(self, body):
#         self.body = body
#
#
# class Auto(Wheels, Engine, Body):
#     def __init__(self, wheels, engine, body):
#         Wheels.__init__(self, wheels)
#         Engine.__init__(self, engine)
#         Body.__init__(self, body)
#
#     def print_info(self):
#         print(f'Wheels: {self.wheels}\n'
#               f'Engine: {self.engine}\n'
#               f'Body: {self.body}')
#
#
# a = Auto('R18', 'Petrol', 'Sedan')
# a.print_info()

# 3.

# class Pet:
#     def __init__(self, name, s):
#         self.name = name
#         self.s = s
#
#     def sound(self):
#         return f'Sound is {self.s.lower()}'
#
#     def show(self):
#         return f'Name is {self.name}'
#
#     def type_type(self):
#         return f'Type is {self.__class__.__name__.lower()}'
#
#
# class Cat(Pet):
#     def __init__(self, name):
#         Pet.__init__(self, name, 'Meow')
#
#
# class Dog(Pet):
#     def __init__(self, name):
#         Pet.__init__(self, name, 'Af')
#
#
# class Parrot(Pet):
#     def __init__(self, name):
#         Pet.__init__(self, name, 'Krr')
#
#
# class Hamster(Pet):
#     def __init__(self, name):
#         Pet.__init__(self, name, 'Piii')
#
#
# a = Hamster('Sirok')
# print(a.sound())
# print(a.show())
# print(a.type_type())
