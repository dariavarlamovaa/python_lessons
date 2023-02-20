number = int(input('Введите число: '))
if number == 12 or number == 1 or number == 2:
    print('Зима')
elif number == 3 or number == 4 or number == 5:
    print('Весна')
elif number == 6 or number == 7 or number == 8:
    print('Лето')
elif number == 9 or number == 10 or number == 11:
    print('Осень')
else:
    print('Ошибка!')

x = int(input('Ведите сколько секунд прошло с начала дня: '))
y = input("В каком виде представить время: в часах; в минутах; в секундах?")
if y == "в часах":
    print(f"До полуночи осталось {(24 * 60 * 60 - x) // (60 * 60)} часов")
if y == "в минутах":
    print(f"До полуночи осталось {(24 * 60 * 60 - x) // 60} мин")
if y == "в секундах":
    print(f"До полуночи осталось {(24 * 60 * 60 - x)} сек")

married = True
if not married:
    print('not married')
else:
    print('married')

num = input('Введите шестизначное число: ')
if len(num) != 6:
    print('Error')
elif int(num[0]) + int(num[1]) + int(num[2]) == int(num[3]) + int(num[4]) + int(num[5]):
    print("Lucky")
else:
    print('Not lucky')
