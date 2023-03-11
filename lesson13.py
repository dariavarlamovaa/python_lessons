# Замыкания - closure
# def outer(par):
#     loc = par
#
#     def inner():
#         return loc
#
#     return inner
#
#
# var = 1
# fun = outer(var)
# print(fun())


# def make_closure(par):
#     loc = par
#
#     def power(p):
#         return p ** loc
#     return power
#
#
# func_sqr = make_closure(2)
# func_cub = make_closure(3)
# print(func_sqr(2), func_cub(2))

# 1.
# def func(char):
#
#     def func_2(strr):
#         print(char + strr + char)
#     return func_2
#
#
# pretty_stars = func('*')
# pretty_stars('Name')

# Пространство имен
# num = 0
# sqrs = [1, 2, 3, 4]
#
#
# def create():
#     global num
#     num += 5
#     sqrs.append(25)
#     print(sqrs)
#     print(num)
#
#
# create()
# create()


# def new():
#     n = 5
#     def create():
#         n = 10
#         def delete():
#             nonlocal n
#             print(n)
#         delete()
#     create()
#
# new()

# 1.
# def counter():
#     n = 0
#     def increase():
#         nonlocal n
#         n += 1
#         print(n)
#     return increase
#
# c = counter()
# c()
# c()

# 2.
# def get_average():
#     c = 0
#     summ = 0
#     def av(n):
#         nonlocal summ, c
#         c += 1
#         summ += n
#         print(summ/c)
#     return av
#
# avg = get_average()
# avg(10)
# avg(20)
# avg(30)

# 3.
# def password_protected(password):
#
#     def sensitive_function(p):
#         return "you have accessed a sensitive function!" if password == p else "error: incorrect password"
#     return sensitive_function
#
#
# protected_func = password_protected('abc123')
# print(protected_func('abc123'))
# print(protected_func('incorrect_password'))
# print(protected_func('blabla'))

# or

# def sensitive_password():
#     return "you have accessed a sensitive function!"
#
#
# def password_protected(password):
#     def inner(pw):
#         if pw == password:
#             return sensitive_password()
#         return 'error: incorrect password'
#
#     return inner
#
#
# pr_func = password_protected('1bc')
# print(pr_func('1bc'))
# print(pr_func('blabla'))

# 4.
# def memorize(f):
#     cache = {}
#
#     def inner(*parameters):
#         if parameters not in cache:
#             cache[parameters] = f(*parameters)
#         return cache[parameters]
#     return inner
#
#
# def slow_add(x, y):
#     print('computing...')
#     return x + y
#
#
# fast_add = memorize(slow_add)
# print(fast_add(1, 2))
# print(fast_add(1, 2))
# print(fast_add(3, 9))


# 5.
# def g():
#     y = 1
#     def inner(x):
#         nonlocal y
#         y += x
#         return y
#     return inner
#
#
# g_inner = g()
# print(g_inner(2))