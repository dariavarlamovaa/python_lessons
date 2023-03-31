# Регулярные выражения(regular expressions, regexp/regex/re) - шаблоны строк
import re

#
# name = input('enter your name: ')
# text = 'hello, my friend. i`d like to go shopping.'
#
# result = re.match('Sasha', name)
# result2 = re.search('Sasha', name)
# result3 = re.findall('Sasha', name)
# result4 = re.fullmatch('Sasha', name)
# print(result.group())
# print(result2.string)
# print(re.split('[.,?`\s]+', text))

# ----------------------

# name = input('введите число из 1: ')
# res = re.search('1{3}', name)
# res = re.search('1{1,3}', name)
# res = re.search('1{5,}', name)
# res = re.search('1{,3}', name)
# res = re.search('1?}', name)
# res = re.search('1*', name)
# res = re.search('1+', name)
# res = re.search('1+.2', name)
# res = re.search('[13]+', name)
# res = re.search('[1-9]', name)
# res = re.search('1{3}', name)
#
#
# print(res)


# ----------------------
# name = '45 54'
# res = re.search('\d+', name)
# print(res)

# 1.
# hour = 'Час в 24-часовом формате от 00 до 23. ' \
#        '2021-06-15Т21:45. Минуты, в диапазоне от ' \
#        '00 до 59. 2021-06-15Т01:09.'
# res = re.finditer('([0-2][0-3]|[0-1][0-9]):[0-5][0-9]', hour)
# for i in res:
#     print(i)

# 2.
# phone = '74994564578'
# res = re.fullmatch('\+?7\d{10}', phone)
# print(res.group())

# 3.
# emails = ['123456@i.ru', '123_456@ru.name.ru', 'login@i.ru', 'norwH-1@i.ru', 'login.3@i.ru', 'Login.3-67@i.ru', '1login@ru.name.ru']
# for email in emails:
#     res = re.fullmatch('[\w.-]+@[\w.]*\.ru', email)
#     print(res.group())

# 4.
# text = '(в русском языке встречаются названия питон[16] ' \
#        'или пайтон[17]) — высокоуровневый язык программирования ' \
#        'общего назначения с динамической строгой типизацией ' \
#        'и автоматическим управлением памятью[18] [19]'
# res = re.findall('\[\d+]', text)
# print(res)

# 5.
# date = input('enter the date in dd-mm-YYYY: ')
# res = re.fullmatch('(0[1-9]|[1-2]\d|3[01])-(0[1-9]|1[0-2])-\d{4}', date)
# print(res)

# task 1 from habr.com
# nums = 'С227НА777', 'КУ22777', 'Т22В7477', 'М227К19У9', ' С227НА777'
# for r in nums:
#     if re.fullmatch(r'\w{1,2}\d{3}\w{2}\d{3}', r):
#         print('Private')
#     elif re.fullmatch(r'\w{1,2}\d{3}\d{2}', r):
#         print('Taxi')
#     else:
#         print('Fail')

# task 2 from habr.com
# text = 'Он --- серо-буро-малиновая редиска!!', '>>>:->', 'А не кот.', 'www.kot.ru'
# count = []
# for t in text:
#     res = re.findall(r"\b[\w-]+\b", t)
#     count.extend(res)
# print(len(count))

# task 3 from habr.com
# text = "Иван Иванович! Нужен ответ на письмо от ivanoff@ivan-chai.ru. Не забудьте поставить в копию serge'o-lupin@mail.ru- это важно."
# text2 = 'NO: foo.@ya.ru, foo@.ya.ru PARTLY: boo@ya_ru, -boo@ya.ru-, foo№boo@ya.ru'
# res = re.findall(r"[\w.'_+-]+@[\w.-]+\.ru", text)
# r = re.findall(r"[\w+]+@[a-z]+\.?r?u?", text2)
# print(res)
# print(r)