# SOLID - пять основных принципов дизайна создания классовой архитектуры

# ---------------------- 1. S - Single Responsibility ----------------------
# Принцип единственной ответственности - у объекта экземпляра
# класса должна быть только одна обязанность, решение которой
# полностью входит в тело класса.

# class UserAccount:
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# class UserDB:
#     def __init__(self, password):
#         self.password = password
#
#     def get_name(self):
#         pass


# ---------------------- 2. Open - Closed----------------------
# Принцип открытости - закрытости - программируемые сущности (классы,
# функции, модули) должны быть открыты для расширения, но закрыты для изменений.

# class DiscountVIP:
#     def __init__(self, price):
#         self.price = price
#
#     def give_discount(self):
#         return self.price * (1 - 0.1)
#
#
# class DiscountFav(DiscountVIP):
#     def give_discount(self):
#         return self.price * (1 - 0.2)


# ---------------------- 3. L - Liskov substitution principle ----------------------
# Принцип подстановки Барбары Лисков - сущности, которые используют
# базовый тип данных, должны иметь возможность использовать подтипы
# базового типа, не зная об этом.

# class IntegerNumber:
#     def __init__(self, value):
#         self.value = int(value)
#
#     def __str__(self):
#         return f'{self.value}'
#
#
# def multiply_string(string: str, num: IntegerNumber):
#     try:
#         return string * num.value
#     except TypeError as e:
#         if 'float' in repr(e):
#             return string * int(num.value)
#
#
# class FloatNumber(IntegerNumber):
#     def __init__(self, value):
#         self.value = value
#
# a = IntegerNumber(5.5)
# b = FloatNumber(5.5)
# print(multiply_string('hi', a))
# print(multiply_string('hi', b))

# ---------------------- 4. I - Interface Substitution Principle ----------------------
# Принцип разделения интерфейса = клиенты не должны зависеть от
# функции, которые они не используют.

# from abc import ABC, abstractmethod
#
#
# class CallingDevice(ABC):
#     @abstractmethod
#     def make_call(self):
#         pass
#
#
# class MessagingDevice(ABC):
#     @abstractmethod
#     def send_message(self):
#         pass
#
#
# class InternetBrowsingDevice(ABC):
#     @abstractmethod
#     def browse_internet(self):
#         pass
#
#
# class OldPhone(MessagingDevice, CallingDevice):
#     def make_call(self):
#         pass
#
#     def send_message(self):
#         pass
#
#
# class NewPhone(MessagingDevice, CallingDevice, InternetBrowsingDevice):
#     def make_call(self):
#         pass
#     def send_message(self):
#         pass
#     def browse_internet(self):
#         pass


# ---------------------- 5. D - Dependency Inversion Principle ----------------------
# Принцип инверсии зависимостей - модули верхних уровней
# не должны зависеть от модулей нижних уровней. А оба
# типа модулей должны зависеть от абстракции. Сами абстракции
# не должны зависеть от деталей реализации, а детали реализаций
# должны зависеть от абстракции.

# ---------- плохая реализация --------

# class Cash:
#     def pay(self, amount):
#         pass
#
#
# class Shop:
#     def do_payment(self, cash, amount):
#         cash.pay(amount)  # класс Shop зависит от класса Cash

# ---------- хорошая реализация --------


# class Payment:
#     def do_transaction(self, amount):
#         raise NotImplementedError
#
#
# class Cash(Payment):
#     def do_transaction(self, amount):
#         pass
#
#
# class ApplePay(Payment):
#     def do_transaction(self, amount):
#         pass
#
#
# class Shop:
#     def do_payment(self, payment, amount):
#         payment.do_transaction(amount)


# ------------------- task -------------------

# from abc import ABC, abstractmethod
#
#
# class PizzaBase(ABC):
#     @abstractmethod
#     def get_cost(self):
#         pass
#
#
# class PizzaBase25cm(PizzaBase):
#     @property
#     def get_cost(self):
#         return 1
#
#     def __str__(self):
#         return 'Основа для пиццы - 25 см'
#
#
# class PizzaBase30cm(PizzaBase):
#     @property
#     def get_cost(self):
#         return 1.44
#
#     def __str__(self):
#         return 'Основа для пиццы - 30 см'


# class Topping:
#     def __init__(self):
#         self.name = self.__class__.__name__.lower()
#
#     def __str__(self):
#         return self.name
#
#
# class Toppings:
#     data = {'Cheese': 10, 'Tomatoes': 15, 'Pepperoni': 20, 'Bacon': 25, 'Mushrooms': 30,
#             'Olives': 25, 'Chicken': 20, 'Pineapple': 20}
#
#     toppings = {}
#
#     @staticmethod
#     def init_toppings():
#         for key, value in Toppings.data.items():
#             Toppings.toppings[key] = (type(key, (Topping,), {'cost': value}))


# class Pizza:
#     def __init__(self, base, *toppings):
#         self.base = base
#         self.toppings = toppings
#
#     @property
#     def get_cost(self):
#         return sum((top.get_cost for top in self.toppings)) * self.base.get_cost


# class PizzaTemplates:
#     @staticmethod
#     def margherita(base=PizzaBase25cm()):
#         return Pizza(base, Toppings.toppings['Cheese'],
#                      Toppings.toppings['Tomatoes'])
#
#     @staticmethod
#     def pepperoni(base=PizzaBase25cm()):
#         return Pizza(base, Toppings.toppings['Pepperoni'],
#                      Toppings.toppings['Cheese'])
#
#     @staticmethod
#     def bacon_mushrooms(base=PizzaBase25cm()):
#         return Pizza(base, Toppings.toppings['Mushrooms'],
#                      Toppings.toppings['Bacon'], Toppings.toppings['Cheese'])


# class Pizzeria:
#     def __init__(self):
#         self.solid_pizzas = 0
#         self.revenue = 0
#         self.profit = 0
#         Toppings.init_toppings()
#
#     def run(self):
#         query = None
#         self.make_an_order()
#         while query != 'Exit':
#             query = input('1. Add pizza to cart\n'
#                           '2. Delete pizza from cart\n'
#                           '3. Show your order\n'
#                           '4. Clean the cart\n'
#                           '5. Pay for your order\n'
#                           'Enter the command: ')
#             if query == '1':
#                 self.add_pizza()
#
#     def make_an_order(self):
#         self.cart = []
#
#     @staticmethod
#     def add_pizza():
#         query = input('Choose the command: \n'
#                       '1. Choose an available pizza\n'
#                       '2. Make your own pizza\n')
#         if query == '1':
#             base = 'enter the number of the pizza: \n'
#             templates = list(PizzaTemplates.__dict__.items())
#             for i, pizza in enumerate(templates):
#                 if isinstance(pizza[1], staticmethod):
#                     pizza_name = pizza[0].capitalize()
#                     pizza_toppings = ", ".join(map(str, pizza[1]().toppings))
#                     base += f'{i}. {pizza_name} - {pizza_toppings}\n'
#
#             choice = int(input(base))
#             pizza_maker = templates[choice - 1][1]
#             size = int(input('enter its size (25/30): '))
#             base = None
#             if size == 25:
#                 pizza = pizza_maker(PizzaBase25cm)
#             else:
#                 pizza = pizza_maker(PizzaBase30cm)
#
#
#
#
# def main():
#     app = Pizzeria()
#     app.run()
#
#
# if __name__ == '__main__':
#     main()
