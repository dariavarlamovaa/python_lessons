# Dict - dictionary
# a = {1: 2, 3: 4, '5': 4}
# print(a)
# print(a.keys())
# print(a.values())
# print(a.items())
#
# for key, value in a.items():
#     print(f'{key}: {value}')
#
# for key in a.keys():
#     print(f'{key}: {a[key]}')
#
# number = 4
# print([key for key, value in a.items() if value == number])
# print(a.pop(1))
# print(a)
# a.popitem()
# print(a)
# print(a.setdefault(0, 0))
# print(a.get(3))
# a.setdefault(9, 3)
# print(a)
# print(a.fromkeys('5', 0))
# print(a)

# 1.
# a = 1
# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# for v in d.values():
#     a *= v
# print(a)

# or
# for key in d:
#     a *= d[key]
# print(a)

# 2.
# veg_dict = {}
# for i in range(1, 5):
#     veg = input('enter the vegetable: ')
#     veg_dict[i] = veg
# print(veg_dict)
# veg_dict.pop(int(input('enter the el to del: ')))
# print(veg_dict)

# or
# veggies = dict([(i, input('enter the veg: ')) for i in range(1, 5)])
# print(veggies)
# del veggies[int(input('enter the el to del: '))]
# print(veggies)

# 3.
# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# x.update(y)
# print(x)

# 4.
# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# d2 = {'name': d.pop('name'), 'salary': d.pop('salary')}
# print(d)
# print(d2)

# 5.
# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# d['location'] = d.pop('city')
# print(d)

# 6.
# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# print(dict(list(d.items())[:2]))
# # or
# new_data = {k: d[k] for i, k in enumerate(d) if i < 2}
# print(new_data)
