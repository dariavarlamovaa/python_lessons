# from jinja2 import Template

# --------------------------
# name = "Ivan"
# age = 30
#
# tm = Template('My name is {{ name }}. I am {{ age }} years old.')
#
# msg = tm.render(name=name, age=age)
# print(msg)

# --------------------------
# person = {
#     'name': 'Ivan',
#     'age': 30
# }
#
# tm = Template('My name is {{ p.name }}. I am {{ p.age }} years old.')
# msg = tm.render(p=person)
# print(msg)

# --------------------------
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
#
# person = Person('Ivan', 30)
# tm = Template('My name is {{ p.name }}. I am {{ p.get_age() }} years old.')
# msg = tm.render(p=person)
# print(msg)

# --------------------------
# data = '''{% raw %}Модуль Jinja вместо
# определения {{ name }}
# подставит соответствующее значение. {% endraw %}'''
#
# tm = Template(data)
# msg = tm.render()
# print(msg)

# -------------------------- ESCAPING (сырая HTML разметка - экранирование)--------------------------
# link = '''В HTML-документе ссылка определяется так
# <a href="#">Ссылка</a>'''
#
# tm = Template('{{ link | e }}')
# msg = tm.render(link=link)
# print(msg)

# -------------------------- Циклы for и условия if elif else --------------------------
# cities = [
#     {'id': 1, 'name': 'Москва'},
#     {'id': 2, 'name': 'Санкт-Петербург'},
#     {'id': 3, 'name': 'Петрозаводск'},
#     {'id': 4, 'name': 'Сортавала'}
# ]
#
# data = """
# {%- for city in cities -%}
#     {%- if city.id > 2 -%}
#         <p>{{ city.id }} {{ city.name }}</p>
#     {%- elif city.name == 'Москва' -%}
#         <h1>{{ city.name }}</h1>
#     {% endif %}
# {% endfor %}
# """
#
# tm = Template(data)
# msg = tm.render(cities=cities)
# print(msg)

# 1.
# menu = [
#     {'url': 'index', 'name': 'Главная'},
#     {'url': 'news', 'name': 'Новости'},
#     {'url': 'about', 'name': 'О компании'},
#     {'url': 'shop', 'name': 'Магазин'},
#     {'url': 'contacts', 'name': 'Контакты'}
# ]
#
# tm = Template('''
# <ul>
# {% for el in menu -%}
#     {%- if el.url == 'index' -%}
#       <li><a href="/{{ el.url }}"class="active">{{ el.name }}</a></li>
#     {%- else -%}
#       <li><a href="/{{ el.url }}">{{ el.name }}</a></li>
#     {%- endif %}
# {% endfor -%}
# </ul>
# ''')
# msg = tm.render(menu=menu)
# print(msg)


# -----------------------
# cars = [
#     {'name': 'Volvo', 'price': 333},
#     {'name': 'Lada', 'price': 222},
#     {'name': 'Toyota', 'price': 444},
#     {'name': 'Lexus', 'price': 555},
#     {'name': 'Volvo', 'price': 111}
# ]

# tm = Template('Результат фильтра: {{ cars | sum(attribute="price") }}')
# tm = Template('Результат фильтра: {{ cars | max(attribute="price") }}')
# tm = Template('Результат фильтра: {{ (cars | min(attribute="price")).name }}')
# tm = Template('Результат фильтра: {{ cars | random }}')
# tm = Template('Результат фильтра: {{ cars | replace("o", "e") }}')
# msg = tm.render(cars=cars)
# print(msg)

# ----------------------
# persons = [
#     {'name': 'Leo', 'year': 18, 'weight': 80},
#     {'name': 'Nick', 'year': 19, 'weight': 72.9},
#     {'name': 'Alex', 'year': 20, 'weight': 100.2},
# ]
#
# tm = """
# {%- for u in users -%}
#     {% filter title %} {{ u.name }} human {% endfilter %}
#     {% filter random %} {{ u.weight }} {% endfilter %}
# {% endfor -%}"""
#
# tm = Template(tm)
# msg = tm.render(users=persons)
# print(msg)

# ----------------------
# html = """
# {% macro input(name, value='', type='text', size=20) %}
#     <input type="{{ type }}" name=" {{ name }}" value=" {{ value }}" size=" {{ size }}">
# {% endmacro %}
#
# {% for name in ['username', 'email', 'password'] %}
#     <p>{{ input(name) }}</p>
# {% endfor %}
# """
# tm = Template(html)
# msg = tm.render()
# print(msg)

# 2.
# html = """
# {%- macro input(name, placeholder, type='text') -%}
#     <input type="{{ type }}" name="{{ name }}" placeholder="{{ placeholder }}">
# {%- endmacro -%}
# <p>{{ input('firstname', 'Имя') }}</p>
# <p>{{ input('lastname', 'Фамилия') }}</p>
# <p>{{ input('address', 'Адрес') }}</p>
# <p>{{ input('phone', 'Телефон', 'tel') }}</p>
# <p>{{ input('email', 'Почта', 'email') }}</p>
# """
#
# tm = Template(html)
# msg = tm.render()
# print(msg)

# ----------------------
# persons = [
#     {'name': 'Leo', 'year': 18, 'weight': 80},
#     {'name': 'Nick', 'year': 19, 'weight': 72.9},
#     {'name': 'Alex', 'year': 20, 'weight': 100.2},
# ]
#
# html = """
# {%- macro list_users(users) -%}
# <ul>
#     {%- for u in users %}
#         <li>{{ u.name }} {{ caller(u) }}</li>
#     {%- endfor %}
# </ul>
# {%- endmacro -%}
#
# {% call(user) list_users(users) %}
#     <ul>
#         <li>age: {{ user.year }}</li>
#         <li>weight: {{ user.weight }}</li>
#     </ul>
# {% endcall %}
# """
#
# tm = Template(html)
# msg = tm.render(users=persons)
# print(msg)

# ----------------------
# from jinja2 import Environment, FileSystemLoader
#
# file_loader = FileSystemLoader('templates')
#
# env = Environment(loader=file_loader)
#
# persons = [
#     {'name': 'Leo', 'year': 18, 'weight': 80},
#     {'name': 'Nick', 'year': 19, 'weight': 72.9},
#     {'name': 'Alex', 'year': 20, 'weight': 100.2},
# ]
#
# tm = env.get_template('main.html')
#
# msg = tm.render(users=persons, title='About Jinja')
# print(msg)

# ----------------------
# from jinja2 import Environment, FileSystemLoader
#
# file_loader = FileSystemLoader('templates')
#
# env = Environment(loader=file_loader)
#
# tm = env.get_template('about.html')
# subs = ['Культура', 'Наука', 'Спорт']
# msg = tm.render(list_table=subs)
#
# print(msg)
