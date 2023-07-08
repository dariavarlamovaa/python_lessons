# UNIT TESTS


# assert condition, message

# password = input('enter your password: ')
# assert password == '1234', 'Incorrect password'

# ------------------------- example -------------------------

# def sum_sum(*args):
#     return sum(args)
#
#
# def test_sum_sum():
#     result = ''
#     try:
#         assert sum_sum(1, 2, 3) == 6, 'Result with arguments 1, 2, 3 mush be 6'
#         result += '1. OK\n'
#     except AssertionError as e:
#         result += f'1. Failed({e})\n'
#
#     try:
#         assert sum_sum() == 0, 'Result without arguments must be 0'
#         result += '2. OK\n'
#     except AssertionError as e:
#         result += f'2. Failed({e})\n'
#
#     try:
#         assert sum_sum(-5, 5, 0) == 0, 'Result with arguments -5, 5, 0 mush me 0'
#         result += '3. OK\n'
#     except AssertionError as e:
#         result += f'3. Failed({e})\n'
#
#     print(result)
#
#
# test_sum_sum()


# -----------------------
# import unittest


#
#
# def sum_sum(*args):
#     return sum(args)
#
#
# class TestSumSum(unittest.TestCase):
#     def test_sum_sum(self):
#         self.assertEqual(sum_sum(1, 2, 3), 6, 'Result with arguments 1, 2, 3 must be 6')
#         self.assertEqual(sum_sum(), 0, 'Result without arguments must be 0')
#         self.assertEqual(sum_sum(-5, 5, 0), 0, 'Result with arguments -5, 5, 0 must me 0')
#
#
# if __name__ == '__main__':
#     unittest.main()

# task 1.
#
# from fraction import Fraction
#
#
# class TestFraction(unittest.TestCase):
#     def setUp(self) -> None:  # устанавливаем значения
#         self.fr1 = Fraction(1, 2)
#         self.fr2 = Fraction(2, 3)
#
#     def tearDown(self) -> None:
#         pass  # чтобы удалить или очистить
#
#     def test_add(self):
#         self.assertEqual('7/6', str(self.fr1 + self.fr2), 'Result with arguments 1/2 and 2/3 must be 7/6')
#
#     def test_sub(self):
#         self.assertEqual('-1/6', str(self.fr1 - self.fr2), 'Result with arguments 1/2 and 2/3'
#                                                            ' must be -1/6')
#
#     def test_mul(self):
#         self.assertEqual('2/6', str(self.fr1 * self.fr2), 'Result with arguments 1/2 and 2/3'
#                                                           ' must be 2/6')
#
#     def test_div(self):
#         self.assertEqual('3/4', str(self.fr1 / self.fr2), 'Result with arguments 1/2 and 2/3'
#                                                           ' must be 3/4')
#
#
# if __name__ == '__main__':
#     unittest.main()

# class Calculator:
#     @staticmethod
#     def add(num1, num2):
#         return num1 + num2
#
#     @staticmethod
#     def sub(num1, num2):
#         return num1 - num2
#
#     @staticmethod
#     def mul(num1, num2):
#         return num1 * num2
#
#     @staticmethod
#     def div(num1, num2):
#         try:
#             return round(num1 / num2, 4)
#         except ZeroDivisionError:
#             pass
#
#     @staticmethod
#     def get_max(num1, num2):
#         return max(num1, num2)
#
#     @staticmethod
#     def get_min(num1, num2):
#         return min(num1, num2)
#
#     @staticmethod
#     def get_percent(num1, num2):
#         return num1 * num2 / 100
#
#     @staticmethod
#     def exponentiation(num1, num2):
#         return num1 ** num2
#
#
# class TestCalculator(unittest.TestCase):
#     def setUp(self) -> None:  # устанавливаем значения
#         self.c1 = 5
#         self.c2 = 7
#
#     def test_add(self):
#         self.assertEqual(12, Calculator.add(self.c1, self.c2), 'Result with arguments 5 and 7 must be 12')
#
#     def test_sub(self):
#         self.assertEqual(-2, Calculator.sub(self.c1, self.c2), 'Result with arguments 5 and 7 must be -2')
#
#     def test_mul(self):
#         self.assertEqual(35, Calculator.mul(self.c1, self.c2), 'Result with arguments 5 and 7 must be -2')
#
#     def test_div(self):
#         self.assertEqual(0.7143, Calculator.div(self.c1, self.c2), 'Result with arguments 5 and 7 must be 0.7142')
#
#     def test_max(self):
#         self.assertEqual(7, Calculator.get_max(self.c1, self.c2), 'Result with arguments 5 and 7 must be 7')
#
#     def test_min(self):
#         self.assertEqual(5, Calculator.get_min(self.c1, self.c2), 'Result with arguments 5 and 7 must be 5')
#
#     def test_percent(self):
#         self.assertEqual(0.35, Calculator.get_percent(self.c2, self.c1), 'Result with arguments 7 and 5% must be 0.35')
#
#     def test_exponentiation(self):
#         self.assertEqual(16807, Calculator.exponentiation(self.c2, self.c1),
#                          'Result with arguments 7 and 5 must be 16807')
#
#
# if __name__ == '__main__':
#     unittest.main()
