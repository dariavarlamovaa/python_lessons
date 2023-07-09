# -------------------------------------- LIST TASKS --------------------------------------
# task fibonacci

# cache = {}


# def get_lst(n):
#     lst = []
#
#     def fibonacci(n):
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         if n in cache:
#             return cache[n]
#         cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
#         return cache[n]
#
#     for i in range(n):
#         lst.append(fibonacci(i))
#     return lst


# print(get_lst(5))


# task anagrams
# def find_anagrams(words: list):
#     anagrams = []
#     for i in range(len(words)):
#         for j in range(i+1, len(words)):
#             new_lst = ''.join(sorted(words[i]))
#             new_lst2 = ''.join(sorted(words[j]))
#             if new_lst == new_lst2:
#                 anagrams.append((words[i], words[j]))
#
#     return anagrams
#
#
# print(find_anagrams(['tok', 'kot', 'arod']))

# task compress
# def compress_file(filename):
#     with open(filename, 'r') as f:
#         data = f.read()
#     dict_symbol = ""
#     total = 0
#     for i in range(len(data)):
#         if i < len(data) - 1 and data[i] == data[i + 1]:
#             total += 1
#         else:
#             dict_symbol += data[i]
#             if total > 1:
#                 dict_symbol += str(total)
#             total = 1
#     with open('b.txt', 'w') as out:
#         out.write(dict_symbol)
#
#
# compress_file('a.txt')

# task
# def file_read_write(input_filename=None, output_filename=None):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if input_filename is not None:
#                 f1 = open(input_filename)
#                 result = func(f1, *args, *kwargs)
#                 f1.close()
#             if output_filename is not None and input_filename is not None:
#                 f1 = open(input_filename)
#                 f2 = open(output_filename)
#                 result = func(f1, f2, *args, *kwargs)
#                 f2.close()
#             return result
#
#         return wrapper
#
#     return decorator
#
#
# @file_read_write(input_filename='a.txt')
# def print_data(filename):
#     print(filename.read())
#
#
# @file_read_write(input_filename='a.txt', output_filename='b.txt')
# def write_data(filename1, filename2):
#     filename2.write(filename1.read())
#
#
# print_data()


# -------------------------------- OOP TASKS --------------------------------
# task 1


# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'{self.__class__.__name__}: ({self.x}, {self.y})'
#
#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Vector(x, y)
#
#     def __sub__(self, other):
#         x = self.x - other.x
#         y = self.y - other.y
#         return Vector(x, y)
#
#     def __mul__(self, num: int | float):
#         x = self.x * num
#         y = self.y * num
#         return Vector(x, y)
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#
#     def __lt__(self, other):
#         return self.x ** 2 + self.y ** 2 < other.x ** 2 + other.y ** 2
#
#
# v1 = Vector(2, 5)
# v2 = Vector(1, 4)
# c = v1 + v2
# d = v1 - v2
# e = v1 * 5
# print(c)
# print(d)
# print(e)
# print(v1 == v2)
# print(v1 < v2)


# task 2
# import random
#
#
# def retry(max_retries):
#     count = 0
#
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             nonlocal count
#             while count < max_retries:
#                 try:
#                     return func(*args, **kwargs)
#                 except:
#                     print('Exception detected....connecting')
#                     count += 1
#
#         return wrapper
#
#     return decorator
#
#
# class DatabaseConnection:
#     @staticmethod
#     @retry(3)
#     def connect():
#         connection_num = random.randint(1, 100)
#         if connection_num < 50:
#             print('Connecting to database....Connected')
#         else:
#             raise Exception
#
#
# d = DatabaseConnection
# d.connect()

# task 3
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print('Животное издает какой-то звук')
#
#
# class Cat(Animal):
#     def speak(self):
#         super().speak()
#         print(f'Появился {self.name}')
#         print('Мяу')
#
#
# class Dog(Animal):
#     def speak(self):
#         super().speak()
#         print(f'Появился {self.name}')
#         print('Гав')
#
#
# gang = [Cat('Фрося'), Dog('Шарик')]
# for animal in gang:
#     animal.speak()


# task 4
# import datetime
# from abc import ABC, abstractmethod
#
#
# def logger(func):
#     def decorator(*args, **kwargs):
#         msg = f'{datetime.datetime.now()}. Function was called\n'
#         with open('log.txt', 'a') as log:
#             log.write(msg)
#             result = func(*args, **kwargs)
#             log.write(f'The result is {result}\n')
#             return result
#
#     return decorator
#
#
# class Shape(ABC):
#     @abstractmethod
#     @logger
#     def area(self):
#         pass
#
#
# class Rectangle(Shape):
#     def __init__(self, a: int, b: int):
#         self.a = a
#         self.b = b
#
#     @property
#     @logger
#     def area(self):
#         return self.a * self.b
#
#
# class Circle(Shape):
#     def __init__(self, radius: int):
#         self.radius = radius
#
#     @property
#     @logger
#     def area(self):
#         return 3.14 * self.radius ** 2
#
#
# r = Rectangle(3, 5)
# c = Circle(5)
# print(r.area)
# print(c.area)


# -------------------------------------- PATTERNS TASKS --------------------------------------

# task 1
# class Singleton:
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             cls._instance = super().__new__(cls)
#         cls.__init__(cls._instance, *args, *kwargs)
#         return cls._instance
#
#     def __init__(self):
#         pass
#
#
# class DatabaseConnection(Singleton):
#     def __init__(self, x):
#         super().__init__()
#         self.x = x
#
#
# d = DatabaseConnection(5)
# d2 = DatabaseConnection(6)
# print(d.x)
# print(d2.x)


# task 2
# class Animal:
#     def __init__(self, sound):
#         self.sound = sound
#
#
# class Dog(Animal):
#     def __init__(self):
#         super().__init__('Bark')
#
#
# class Bird(Animal):
#     def __init__(self):
#         super().__init__('Tweet')
#
#
# class Cat(Animal):
#     def __init__(self):
#         super().__init__('Meow')
#
#
# class AnimalFactory:
#     @staticmethod
#     def create_animal(animal_type):
#         dict_animals = {'dog': Dog, 'bird': Bird, 'cat': Cat}
#         return dict_animals.get(animal_type.lower())()
#
#
# farm = ['dog', 'bird', 'cat', 'sheep']
# for animal in farm:
#     print(AnimalFactory.create_animal(animal).sound)

# task 3

# class Wheels:
#     def __str__(self):
#         return 'Wheel 21'
#
#
# class Engine:
#     def __str__(self):
#         return 'Engine P240'
#
#
# class Body:
#     def __str__(self):
#         return 'Body green'
#
#
# class Car:
#     def __init__(self):
#         pass
#
#
# class CarBuilder:
#     def __init__(self):
#         self.car = Car()
#
#     def get_wheels(self):
#         return Wheels()
#
#     def get_engine(self):
#         return Engine()
#
#     def get_body(self):
#         return Body()
#
#     def build_car(self):
#         self.car.wheels = self.get_wheels()
#         self.car.engine = self.get_engine()
#         self.car.body = self.get_body()
#
#     def get_car(self):
#         return self.car
#
#
# builder = CarBuilder()
# builder.build_car()
# car1 = builder.get_car()
# print(car1)


# task 4

# class CreditCardStrategy:
#     @staticmethod
#     def pay():
#         print('Paying via card.....Approved')
#
#
# class PayPalStrategy:
#     @staticmethod
#     def pay():
#         print('Payment via PayPal.....Approved')
#
#
# class PaymentProcessor:
#     def __init__(self, strategy=CreditCardStrategy):
#         self.strategy = strategy
#
#     def do_transaction(self):
#         self.strategy.pay()
#
#     def set_strategy(self):
#         choice = input('enter the strategy: 1-via card, 2-via PayPal: ')
#         dict_strategy = {'1': CreditCardStrategy, '2': PayPalStrategy}
#         if choice in dict_strategy:
#             self.strategy = dict_strategy.get(choice)()
#         else:
#             print('error')
#
#
# p = PaymentProcessor()
# p.do_transaction()
# p.set_strategy()
# p.do_transaction()


# task 5

# class SocialMediaAccount:
#     @staticmethod
#     def special_post():
#         return 'This is the original post format'
#
#
# class SocialMediaPost:
#     def create_post(self):
#         pass
#
#
# class SocialMediaAdapter:
#     def __init__(self, account: SocialMediaAccount):
#         self.account = account
#
#     def create_post(self):
#         return self.account.special_post()
#
#
# if __name__ == '__main__':
#     account = SocialMediaAccount()
#     adapter = SocialMediaAdapter(account)
#     post = adapter.create_post()
#     print(post)


# task 6

# from abc import ABC, abstractmethod
#
#
# class Homework(ABC):
#     @abstractmethod
#     def do_homework(self):
#         raise NotImplementedError
#
#
# class MathHomework(Homework):
#     def do_homework(self):
#         return 'Math homework is done'
#
#
# class HomeworkProxy(Homework):
#     def __init__(self):
#         self.math_homework = MathHomework()
#
#     def do_homework(self):
#         string = 'You have received new math homework\n'
#         string += self.math_homework.do_homework()
#         return string
#
#
# h = HomeworkProxy()
# h1 = h.do_homework()
# print(h1)


# -------------------------------------- SOLID --------------------------------------
# task 1
# S - Single Responsibility Principle - принцип единственной ответственности

# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#
#     def authenticate(self, username, password):
#         pass
#
#     def update_profile(self, username, new_password, email):
#         pass
#
#     def get_user_data(self):
#         pass
#
#
# class UserAuth:
#     @staticmethod
#     def user_auth(username, password):
#         pass
#
#
# class UpdateUserInfo:
#     @staticmethod
#     def update_info(username, new_password, email):
#         pass
#
#
# class GetUserData:
#     @staticmethod
#     def get_data(user:User):
#         return user.__dict__

# task 2
# O - Open-Closed Principle

# class Shape:
#     def calculate_area(self):
#         pass
#
#
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def calculate_area(self):
#         print(self.a * self.b)
#
#
# class Triangle(Shape):
#     def __init__(self, a, height):
#         self.a = a
#         self.height = height
#
#     def calculate_area(self):
#         print(self.a * self.height * 0.5)

# task 3
# L - Liskov Substitution Principle - принцип подстановки Лисков

# class Animal:
#     pass
#
#
# class SoundMakingAnimal(Animal):
#     def make_sound(self):
#         pass
#
#
# class Dog(SoundMakingAnimal):
#     def make_sound(self):
#         print("Woof!")
#
#
# class Cat(SoundMakingAnimal):
#     def make_sound(self):
#         print("Meow!")
#
#
# class Bird(Animal):
#     pass


# task 4
# I - Interface Segregation Principle - принцип разделения интерфейсов
# class PrintDocument:
#     def printing_document(self):
#         pass
#
#
# class ScanDocument:
#     def scanning_document(self):
#         pass
#
#
# class Printer(PrintDocument):
#     @staticmethod
#     def print_document():
#         print('Распечатка документа...')
#
#
# class Scanner(ScanDocument):
#     @staticmethod
#     def scan_document():
#         print('Сканирование документа...')


# task 5
# D - Dependency Inversion Principle
# from abc import ABC, abstractmethod


# class GmailService:
#     def send_email(self, recipient, message):
#         pass
#
#
# class Customer:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.gmail_service = GmailService()
#
#     def notify(self, message):
#         self.gmail_service.send_email(self.email, message)

# =========================== fix ==========================
# class EmailService(ABC):
#     @abstractmethod
#     def send_email(self, recipient, message):
#         pass
#
#
# class GmailService(EmailService):
#     def send_email(self, recipient, message):
#         print(f'Letter was sent via Gmail to {recipient}.\n'
#               f'Message: {message}')
#
#
# class YandexService(EmailService):
#     def send_email(self, recipient, message):
#         print(f'Letter was sent via Yandex to {recipient}.\n'
#               f'Message: {message}')
#
#
# class Customer:
#     def __init__(self, email, email_service: EmailService):
#         self.email = email
#         self.email_service = email_service
#
#     def notify(self, message):
#         self.email_service.send_email(self.email, message)
#
#
# c = Customer('daniil_daniil@mail.ru', YandexService())
# c.notify('Hello')
# c = Customer('daniil_daniil@mail.ru', GmailService())
# c.notify('Hello')


# -------------------------------------- Multiprocessing --------------------------------------
# import threading
#
#
# def print_hi(name):
#     locker.acquire()
#     print(locker.locked())
#     print(f'Oh! Hi, {name}')
#     locker.release()
#     print(locker.locked())
#
#
# locker = threading.Lock()
# thr = threading.Thread(target=print_hi, args=('Leo',))
# thr.start()
# thr.join()
# print('Program finished')
