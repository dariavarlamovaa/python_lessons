# print(f"{'hello':{'%'}^11}")

user_alpha = 0
user_digit = 0
user_str = input('Введите строку: ')
for i in user_str:
    if i.isalpha():
        user_alpha += 1
    if i.isdigit():
        user_digit += 1
print('Количество цифр', user_digit)
print("Количество букв", user_alpha)

# print(input('введите строку: ').count(input('введите символ: ')))

# a, b, c = input('введите строку: '), input('введите слово для поиска: '), input('введите слово для замены: ')
# print(a.replace(b, c))

# user_digits, marks, exc_marks = 0, 0, 0
# a = input('введите текст:')
# for i in a:
#     if i.isdigit():
#         user_digits += 1
#     if i in [',', '.', '!', '?']:
#         marks += 1
#     if i in "!":
#         exc_marks += 1
# print('. '.join(map(lambda x: x.capitalize(), a.split('. '))))
# print('Количество цифр:', user_digits)
# print('Количество знаков препинания:', marks)
# print('Восклицательных знаков:', exc_marks)
