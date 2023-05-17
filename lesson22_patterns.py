# ----------------------------SINGLETON----------------------------------
# Singleton - цель шаблона заключается в следующем:
# --- Обеспечение создания одного и только одного объекта класса
# --- Контроль одновременного доступа к ресурсам, которые являются общими

# class Singleton:
#     def __new__(cls, width, height):
#         if not hasattr(cls, '_instance'):
#             cls._instance = super().__new__(cls)
#         else:
#             print(f'you are resetting {cls.__name__} object attributes')
#         cls.__init__(cls._instance, width, height)
#         return cls._instance
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#
# class New(Singleton):
#     pass
#
#
# a = New(2, 5)
# print(a.width, a.height)
# b = New(3, 4)
# print(b.width, b.height)
# print(id(a))
# print(id(b))

# ---------------------------PROTOTYPE-------------------------------

# Prototype - шаблон проектирования, который решает проблему
# копирования объектов путем делегирования этой
# задачи самим объектам. Все объекты, которые можно копировать,
# должны реализовать метод clone и использовать его для
# получения точных копий самих себя.


# from abc import ABC, abstractmethod
#
#
# class Prototype(ABC):
#
#     @abstractmethod
#     def clone(self):
#         pass
#
#
# class MyObject(Prototype):
#     def __init__(self, arg1, arg2):
#         self.field1 = arg1
#         self.field2 = arg2
#         self.performed_operation = False
#
#     def __operation__(self):
#         self.performed_operation = True
#
#     def clone(self):
#         obj = MyObject(self.field1, self.field2)
#         obj.performed_operation = self.performed_operation
#         return obj


# Шаблон Prototype может быть действительно полезен в
# крупномасштабных приложениях, которые создают
# множество объектов. Иногда копирование уже
# существующего объекта обходится дешевле,
# чем создание нового.

# 1. ------------task-------------
# numbers = list(map(int, input('Введите числа через пробел: ').split()))
# work_file = input('Введите путь к файлу для работы: ')
# open(work_file, 'w').close()
#
#
# class Logger:
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             cls._instance = super().__new__(cls, *args, **kwargs)
#             return cls._instance
#         else:
#             raise NotImplementedError('Нельзя создать больше одного логгера')
#
#     def __init__(self):
#         self.target = None
#         while self.target not in ['экран', 'файл']:
#             self.target = input('Введите, куда писать логи(экран/файл): ')
#         if self.target == 'файл':
#             self.filepath = input('Введите путь к файлу логов: ')
#             open(self.filepath, 'w').close()
#
#     def log_func(self, func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             log_message = f'Функция {func.__name__} была вызвана с аргументами {(*args, *kwargs.items())} ' \
#                           f'и вернула {result}'
#             if self.target == 'экран':
#                 print(log_message)
#             elif self.target == 'файл':
#                 with open(self.filepath, 'a', encoding='utf-8') as f:
#                     f.write('\n' + log_message)
#             return result
#         return wrapper
#
#
# logger = Logger()
#
#
# @logger.log_func
# def save():
#     with open(work_file, 'a') as f:
#         f.write('\n' + ' '.join(list(map(str, numbers))))
#
#
# @logger.log_func
# def find_min_max():
#     minimum, maximum = min(numbers), max(numbers)
#     with open(work_file, 'a') as f:
#         f.write('\n' + str(minimum) + ' ' + str(maximum))
#
#     return minimum, maximum
#
#
# @logger.log_func
# def print_numbers():
#     print(numbers)
#
#
# @logger.log_func
# def print_min_max():
#     print(min(numbers), max(numbers))
#
#
# save()
# print(find_min_max())
# print_numbers()
# print_min_max()

# ---------------------------BUILDER-------------------------------

# Builder Method — это порождающий шаблон проектирования,
# целью которого является отделить построение сложного
# объекта от его представления, чтобы один и тот же
# процесс построения мог создавать разные представления.

# class Robot:
#     def __init__(self):
#         self.bipedal = False
#         self.quadripedal = False
#         self.wheeled = False
#         self.flying = False
#         self.traversal = []
#         self.detection_systems = []
#
#     def __str__(self):
#         string = ""
#         if self.bipedal:
#             string += "BIPEDAL "
#         if self.quadripedal:
#             string += "QUADRIPEDAL "
#         if self.flying:
#             string += "FLYING ROBOT "
#         if self.wheeled:
#             string += "ROBOT ON WHEELS\n"
#         else:
#             string += "ROBOT\n"
#         if self.traversal:
#             string += "Traversal modules installed:\n"
#         for module in self.traversal:
#             string += "- " + str(module) + "\n"
#         if self.detection_systems:
#             string += "Detection systems installed:\n"
#         for system in self.detection_systems:
#             string += "- " + str(system) + "\n"
#         return string
#
#
# class BipedalLegs:
#     def __str__(self):
#         return "two legs"
#
#
# class QuadripedalLegs:
#     def __str__(self):
#         return "four legs"
#
#
# class Arms:
#     def __str__(self):
#         return "arms"
#
#
# class Wings:
#     def __str__(self):
#         return "wings"
#
#
# class Blades:
#     def __str__(self):
#         return "blades"
#
#
# class FourWheels:
#     def __str__(self):
#         return "four wheels"
#
#
# class TwoWheels:
#     def __str__(self):
#         return "two wheels"
#
#
# class CameraDetectionSystem:
#     def __str__(self):
#         return "cameras"
#
#
# class InfraredDetectionSystem:
#     def __str__(self):
#         return "infrared"
#
#
# from abc import ABC, abstractmethod
#
#
# class RobotBuilder(ABC):
#     @abstractmethod
#     def reset(self):
#         pass
#
#     @abstractmethod
#     def build_traversal(self):
#         pass
#
#     @abstractmethod
#     def build_detection_system(self):
#         pass
#
#
# class AndroidBuilder(RobotBuilder):
#     def __init__(self):
#         self.product = Robot()
#
#     def reset(self):
#         self.product = Robot()
#
#     def get_product(self):
#         return self.product
#
#     def build_traversal(self):
#         self.product.bipedal = True
#         self.product.traversal.append(BipedalLegs())
#         self.product.traversal.append(Arms())
#
#     def build_detection_system(self):
#         self.product.detection_systems.append(CameraDetectionSystem())
#
#
# class AutonomousCarBuilder(RobotBuilder):
#     def __init__(self):
#         self.product = Robot()
#
#     def reset(self):
#         self.product = Robot()
#
#     def get_product(self):
#         return self.product
#
#     def build_traversal(self):
#         self.product.wheeled = True
#         self.product.traversal.append(FourWheels())
#
#     def build_detection_system(self):
#         self.product.detection_systems.append(InfraredDetectionSystem())


# builder = AndroidBuilder()
# builder.build_traversal()
# builder.build_detection_system()
# print(builder.get_product())


# builder = AutonomousCarBuilder()
# builder.build_traversal()
# builder.build_detection_system()
# print(builder.get_product())


# Если в полях нашего продукта используются
# относительно стандартные конструкторы, мы
# можем даже создать так называемого директора
# для управления конкретными сборщиками:

# class Director:

#     def make_android(self, builder):
#         builder.build_traversal()
#         builder.build_detection_system()
#         return builder.get_product()
#
#     def make_autonomous_car(self, builder):
#         builder.build_traversal()
#         builder.build_detection_system()
#         return builder.get_product()
#
#
# director = Director()
# builder = AndroidBuilder()
# print(director.make_android(builder))

# Тем не менее, шаблон Builder не имеет большого
# смысла для небольших, простых классов, поскольку
# добавленная логика для их построения просто
# добавляет сложности.

# ---------------------------FACTORY METHOD-------------------------------


# import abc
#
#
# class Shape(abc.ABC):
#     @abc.abstractmethod
#     def calculate_area(self):
#         pass
#
#     @abc.abstractmethod
#     def calculate_perimeter(self):
#         pass
#
#
# class Rectangle(Shape):
#     def __init__(self, height, width):
#         self.height = height
#         self.width = width
#
#     def calculate_area(self):
#         return self.height * self.width
#
#     def calculate_perimeter(self):
#         return 2 * (self.height + self.width)
#
#
# class Square(Shape):
#     def __init__(self, width):
#         self.width = width
#
#     def calculate_area(self):
#         return self.width ** 2
#
#     def calculate_perimeter(self):
#         return 4 * self.width
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def calculate_area(self):
#         return 3.14 * self.radius * self.radius
#
#     def calculate_perimeter(self):
#         return 2 * 3.14 * self.radius

# Шаблон проектирования Factory Method поможет нам
# абстрагировать доступные фигуры от клиента, т. е.
# клиенту не нужно знать все доступные фигуры, а
# нужно только создавать то, что ему нужно во
# время выполнения. Это также позволит нам
# централизовать и инкапсулировать создание объекта.


# class ShapeFactory:
#
#     @staticmethod
#     def create_shape(name):
#         if name == 'circle':
#             radius = input("Enter the radius of the circle: ")
#             return Circle(float(radius))
#
#         elif name == 'rectangle':
#             height = input("Enter the height of the rectangle: ")
#             width = input("Enter the width of the rectangle: ")
#             return Rectangle(int(height), int(width))
#
#         elif name == 'square':
#             width = input("Enter the width of the square: ")
#             return Square(int(width))
#         else:
#             raise ValueError('You cannot create this shape!')
#
#
# factory = ShapeFactory()
# shapes = []
# for i in range(3):
#     shape = input('Input name of shape to create: ').lower()
#     shapes.append(factory.create_shape(shape))
#     print(shapes[-1])
#     print(shapes[-1].calculate_area(), shapes[-1].calculate_perimeter())

# ---------------------------ABSTRACT FACTORY METHOD-------------------------------
# Abstract Factory Method

# from abc import ABC, abstractmethod
#
#
# class Browser(ABC):
#
#     @abstractmethod
#     def create_search_toolbar(self):
#         pass
#
#     @abstractmethod
#     def create_browser_window(self):
#         pass
#
#
# class Messenger(ABC):
#     @abstractmethod
#     def create_messenger_window(self):
#         pass
#
#
# class VanillaBrowser(Browser):
#
#     def create_search_toolbar(self):
#         print("Search Toolbar Created")
#
#     def create_browser_window(self):
#         print("Browser Window Created")
#
#
# class VanillaMessenger(Messenger):
#
#     def create_messenger_window(self):
#         print("Messenger Window Created")
#
#
# class SecureBrowser(Browser):
#
#     def create_search_toolbar(self):
#         print("Secure Browser - Search Toolbar Created")
#
#     def create_browser_window(self):
#         print("Secure Browser - Browser Window Created")
#
#     def create_incognito_mode(self):
#         print("Secure Browser - Incognito Mode Created")
#
#
# class SecureMessenger(Messenger):
#
#     def create_messenger_window(self):
#         print("Secure Messenger - Messenger Window Created")
#
#     def create_privacy_filter(self):
#         print("Secure Messenger - Privacy Filter Created")
#
#     def disappearing_messages(self):
#         print("Secure Messenger - Disappearing Messages Feature Enabled")
#
#
# class AbstractFactory(ABC):
#
#     @abstractmethod
#     def create_browser(self):
#         pass
#
#     @abstractmethod
#     def create_messenger(self):
#         pass
#
#
# class VanillaProductsFactory(AbstractFactory):
#
#     def create_browser(self):
#         return VanillaBrowser()
#
#     def create_messenger(self):
#         return VanillaMessenger()
#
#
# class SecureProductsFactory(AbstractFactory):
#
#     def create_browser(self):
#         return SecureBrowser()
#
#     def create_messenger(self):
#         return SecureMessenger()
#
#
# def main():
#     for factory in (VanillaProductsFactory(), SecureProductsFactory()):
#         product_a = factory.create_browser()
#         product_b = factory.create_messenger()
#         product_a.create_browser_window()
#         product_a.create_search_toolbar()
#         product_b.create_messenger_window()
#
#
# if __name__ == "__main__":
#     main()

# ---------------------------ITERATOR-------------------------------
# Итератор - это поведенческий паттерн, который предоставляет
# последовательный доступ к элементам объекта без раскрытия
# его базовой реализации

# class MyClass:
#     def __init__(self, lst):
#         self.lst = lst
#         self.i = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i == len(self.lst):
#             raise StopIteration
#         result = self.lst[self.i]
#         return result
#
#
# a = MyClass([4, 2, 3, 4, 6])
# for i in a:
#     print(i)


# Метод, позволяющий получить буквы алфавита до конкретной,
# который возвращает итератор
# def alphabets_up_to(letter):
#     for i in range(65, ord(letter) + 1):
#         yield chr(i)
#
#
# alphabets_upto_K = alphabets_up_to('K')
# alphabets_upto_M = alphabets_up_to('M')
#
# for alpha in alphabets_upto_K:
#     print(alpha, end=" ")
# print()
# for alpha in alphabets_upto_M:
#     print(alpha, end=" ")


# Использование встроенных генераторов для повторения поведения
# паттерна "итератор"
# def inBuilt_Iterator1():
#     alphabets = (chr(i) for i in range(65, 91))
#     for alpha in alphabets:
#         print(alpha, end=" ")
#     print()
#
#
# def inBuilt_Iterator2():
#     alphabets = [chr(i) for i in range(97, 123)]
#     for alpha in alphabets:
#         print(alpha, end=" ")
#     print()

#
# inBuilt_Iterator1()
# inBuilt_Iterator2()

# ---------------------------PROXY-------------------------------
# Proxy
# Теоретически ресурсоемкий объект
# class College:
# def studyingincollege(self):
# print("Studying In College....")

# Относительно менее ресурсоемкий прокси,
# выступающий в роли посредника.
# Создает экземпляр объекта College только
# в том случае, если было оплачено обучение.


# class CollegeProxy:
#     def __init__(self):
#         self.feeBalance = 1000
#         self.college = None
#
#     def studyingincollege(self):
#         print("Proxy in action. Checking to see if the balance "
#               "of student is clear or not...")
#         if self.feeBalance <= 500:
#             # Если баланс меньше 500, пускаем ученика
#             # в колледж и позволяем учиться
#             self.college = College()
#             self.college.studyingincollege()
#         else:
#             # В противном случае не пускаем ученика в колледж
#             print("Your fee balance is greater than 500, first pay the fee")


# Создаём прокси
# collegeProxy = CollegeProxy()

# Студент пытается учиться в Колледже с балансом по умолчанию 1000.
# Поскольку он логически не может учиться с балансом в 1000
# то нет смысла создавать объект Колледжа
# collegeProxy.studyingincollege()

# Меняем баланс студента, чтобы он смог учиться в Колледже
# collegeProxy.feeBalance = 100

# Студент пытается учиться в Колледже с балансом в 100. Должно сработать
# collegeProxy.studyingincollege()

# ---------------------------STRATEGY-------------------------------
# 1. Функциональная реализация

# Стратегия вывода на экран
# def console_writer(info):
#     print(info)
#
#
# # Стратегия вывода в файл
# def file_writer(info):
#     with open('log.txt', 'a') as file:
#         file.write(info + '\n')
#
#
# # Интерфейс, работающий со стратегией
# def client(writer):
#     writer('Hello world!')
#     writer('Good bye!')
#
#
# # Код, где пользователь выбирает стратегию
# if input('Записывать в файл?').lower() == 'да':
#     client(writer=file_writer)
# else:
#     client(writer=console_writer)

# Стратегия выбирается пользователем, а функция
# client даже не знает, какой вариант алгоритма
# ей дадут. Она знает лишь то, что writer(info)
# – это некая функция, принимающая строку
# (это и есть общий интерфейс для всех стратегий).
# Таким образом, мы делегируем работу стратегиям,
# скрывая детали реализации каждой из них.


# 2. Объектная реализация

# from abc import ABC, abstractmethod


# Определение общего поведения стратегий
# class BaseStrategy(ABC):
#     @abstractmethod
#     def do_work(self, x, y):
#         pass


# Стратегия 1
# class Adder(BaseStrategy):
#     def do_work(self, x, y):
#         return x + y


# Стратегия 2
# class Multiplicator(BaseStrategy):
#     def do_work(self, x, y):
#         return x * y


# Интерфейс, работающий со стратегией
# class Calculator:
#     def set_strategy(self, strategy: BaseStrategy):
#         self.strategy = strategy
#
#     def calculate(self, x, y):
#         print('Результат:', self.strategy.do_work(x, y))
#
#
# calc = Calculator()
# if input('Вы хотите сложить или умножить числа? Ответ: ').lower() == 'сложить':
#     calc.set_strategy(Adder())
# else:
#     calc.set_strategy(Multiplicator())
# x, y = input('Введите первое число: '), input('Введите второе число: ')
# calc.calculate(int(x), int(y))

# ---------------------------ADAPTER-------------------------------
# Adapter
# Представим, что у нас есть телевизор,
# картинку с которого мы хотим пускать
# на экран. И к нему подключены два устройства:
# игровая консоль и антенна. Но у обоих устройств
# разные функции для получения картинки.
# Таким образом, вариантом решения такой задачи
# может быть добавление классов адаптеров,
# которые бы "адаптировали" разные интерфейсы
# взаимодействия к одному стандарту.

# Игровая консоль
# class GameConsole:
#     def create_game_picture(self):
#         return 'picture from console'


# Антенна
# class Antenna:
#     def create_wave_picture(self):
#         return 'picture from wave'


# Адаптер игровой консоли
# class SourceGameConsole(GameConsole):
#     def get_picture(self):
#         return self.create_game_picture()


# Адаптер антенны
# class SourceAntenna(Antenna):
#     def get_picture(self):
#         return self.create_wave_picture()


# Адаптеры в свою очередь берут на себя перевод
# разных интерфейсов: create_game_picture и
# create_wave_picture и приводят их к одному:
# get_picture.

# Наш телевизор, который просто принимает источник
# в виде адаптера и спокойно вызывает теперь уже общий
# интерфейс в виде get_picture()
# class TV:
#     def __init__(self, source):
#         self.source = source
#
#     def set_source(self, new_source):
#         self.source = new_source
#
#     def show_picture(self):
#         return self.source.get_picture()
#
#
# g = SourceGameConsole()
# a = SourceAntenna()
# tv = TV(g)
# print(tv.show_picture())
# tv.set_source(a)
# print(tv.show_picture())

# 2. ---------task----------
# class FileStrategy:
#     @staticmethod
#     def __out__(obj, value=None):
#         with open(obj.output_filename, 'a', encoding='utf-8') as f:
#             if value:
#                 f.write('\n' + str(value))
#             else:
#                 f.write('\n' + ' '.join(map(str, obj.arr)))
#
#     @staticmethod
#     def __in__(obj):
#         with open(obj.input_filename, 'r', encoding='utf-8') as f:
#             obj.arr = list(map(str, f.read().split()))
#
#
# class ConsoleStrategy:
#     @staticmethod
#     def __out__(obj, value=None):
#         if value:
#             print(value)
#         else:
#             print(*obj.arr)
#
#     @staticmethod
#     def __in__(obj):
#         obj.arr = list(map(int, input('Введите числа через пробел: ').split()))
#
#
# class Strategy:
#     def __init__(self):
#         self.arr = []
#         self.__strategy = None
#         self.input_filename = ''
#         self.output_filename = ''
#
#     @property
#     def strategy(self):
#         return self.__strategy
#
#     @strategy.setter
#     def strategy(self, value):
#         if value == 'файл':
#             self.__strategy = FileStrategy()
#             self.output_filename = input('Введите файл для вывода: ')
#             while True:
#                 self.input_filename = input('Введите файл для ввода: ')
#                 try:
#                     open(self.input_filename, 'r').close()
#                 except FileNotFoundError:
#                     print('Такого файла не существует!')
#                 else:
#                     break
#         elif value == 'экран':
#             self.__strategy = ConsoleStrategy()
#         else:
#             print('Неверно введена стратегия!')
#
#     def max(self):
#         self.strategy.__out__(self, max(self.arr))
#
#     def min(self):
#         self.strategy.__out__(self, min(self.arr))
#
#     def reverse(self):
#         self.arr.reverse()
#         self.strategy.__out__(self)
#
#     def write(self):
#         self.strategy.__out__(self)
#
#     def read(self):
#         self.strategy.__in__(self)
#
#
# a = Strategy()
#
# while True:
#     command = input('Введите номер команды:\n'
#                     '1. Считать данные\n'
#                     '2. Сохранить данные\n'
#                     '3. Найти максимум\n'
#                     '4. Найти минимум\n'
#                     '5. Перевернуть данные\n'
#                     '6. Установить стратегию.\n')
#     if command == '6':
#         a.strategy = input('Введите стратегию(файл/экран): ')
#     elif not a.strategy:
#         print('Сначала выберите стратегию!')
#     elif command == '1':
#         a.read()
#     elif command == '2':
#         a.write()
#     elif command == '3':
#         a.max()
#     elif command == '4':
#         a.min()
#     elif command == '5':
#         a.reverse()
#     else:
#         print('Такой команды не существует!')


# ---------------------------FACADE-------------------------------
# Facade
# Представьте, что у вас есть система со
# значительным количеством объектов. Каждый
# объект предлагает богатый набор методов API.
# С этой системой можно делать много чего, но
# как насчет упрощения интерфейса? Почему бы
# не добавить объект интерфейса, предоставляющий
# хорошо продуманное подмножество всех методов API?
# Фасад!

# Подсистема 1
# class Washing:
#     def wash(self):
#         print("Washing...")


# Подсистема 2
# class Rinsing:
#     def rinse(self):
#         print("Rinsing...")


# Подсистема 3
# class Spinning:
#     def spin(self):
#         print("Spinning...")


# Фасад, предоставляющий доступ к действиям подсистем
# class WashingMachine:
#     def __init__(self):
#         self.washing = Washing()
#         self.rinsing = Rinsing()
#         self.spinning = Spinning()
#
#     def startWashing(self):
#         self.washing.wash()
#         self.startRinsing()
#
#     def startRinsing(self):
#         self.rinsing.rinse()
#         self.spinning.spin()
#
#
# washingMachine = WashingMachine()
# washingMachine.startWashing()


# ---------------------------COMMAND-------------------------------
# Command
# Шаблон Command — это поведенческий шаблон проектирования,
# в котором существует абстракция между объектом,
# который вызывает команду, и объектом, который ее выполняет.

# Например, кнопка вызовет Invoker, который
# вызовет предварительно зарегистрированный Command,
# который выполнит Receiver.

# from abc import ABC, abstractmethod
#
#
# # Абстрактный класс для создания команд
# class Command(ABC):
#     def __init__(self, receiver):
#         self.receiver = receiver
#
#     @abstractmethod
#     def process(self):
#         pass
#
#
# # Конкретная реализация команды
# class CommandImplementation(Command):
#     def __init__(self, receiver):
#         self.receiver = receiver
#
#     def process(self):
#         self.receiver.perform_action()
#
#
# # Объект-получатель
# class Receiver:
#     def perform_action(self):
#         print('Action performed in receiver.')
#
#
# # Объект вызывающий
# class Invoker:
#     def command(self, cmd):
#         self.cmd = cmd
#
#     def execute(self):
#         self.cmd.process()
#
#
# receiver = Receiver()
# cmd = CommandImplementation(receiver)
# invoker = Invoker()
# invoker.command(cmd)  # Наша регистрируемая прослойка - команда
# invoker.execute()
