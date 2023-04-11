# file
# r - read, w - write, a - append(дозапись)
# t - textual, b - bites
# file = open(file='file.txt', mode='r', encoding='utf-8')
# print(file.writable())
# print(file.readable())
# file.write('1, 2, 3\nPython\t...')
# print(file.read())


# ------------------
# file = open(file='file.txt', mode='r+', encoding='utf-8')
# print(file.readable(), file.writable())
# print(file.write('1235'))
# print(file.readline())
# print(file.readline())
# print(file.readlines())
# print(file.write('\nhello'))
# print(file.write('hi\nhow are you?'))

# the correct way to open a file
# with open('file.txt', 'r') as f:
#     f.read()

# -------------------
# import sys
# print(sys.stdin)
# print(sys.stdout)
# print(sys.stderr)
# sys.stderr.close()
# print(1 + '2')

# -------------------
# file = open()
# file.writelines()

# 1.
# with open('file.txt', 'r') as f:
#     # lst = f.readlines()
#     # print(len(lst))
# or
#     count = 0
#     for i in f:
#         count += 1
#     print('count =', count)

# 2.
# file_name = input('enter the file name: ')
# try:
#     with open(file_name, 'r') as file:
#         lines = file.readlines()
#     line = int(input('enter the line number: '))
#     new_line = input('enter the new line: ')
#     lines[line - 1] = new_line + '\n'
#
#     with open(file_name, 'w') as file2:
#         file2.writelines(lines)
# except FileNotFoundError:
#     print('file was not found')
# except ValueError:
#     print('incorrect line number')
# except IndexError:
#     print('there is no string in the file')

# 3.
# from re import split
# with open('file.txt', 'r') as file1:
#     f = file1.read()
# words = split('[,.!?\s\t\n]', f)
#
# with open('file2.txt', 'w') as file2:
#     new = []
#     for word in words:
#         if len(word) == 7:
#             new.append(word)
#     seven = ' '.join(new)
#     file2.write(seven)

# 4.
# with open('file.txt', 'r') as file1, open('file.txt', 'w') as file2:
#     r = file1.readlines()[::-1]
#     flag = False
#     for i, line in enumerate(r):
#         if ',' not in line:
#             flag = True
#             break
#     if flag:
#         r.insert(i, '\n'+ '*' * 12)
#     else:
#         r.insert(0, '\n' +'*' * 12)
#     file2.writelines(r[::-1])

# 5.
# with open('file.txt', 'r') as file1, open('file3.txt', 'r') as bad_words:
#     lines = file1.read().strip()
#     words = bad_words.read().split(', ')
#     for word in words:
#         lines = lines.replace(word, '')
# with open('file2.txt', 'w') as file2:
#     file2.write(lines)

# 6.
# translit_dict = {'ы': 'y', 'ь': "'", 'ъ': "''",
#                  'А': 'A', 'а': 'a',
#                  'Б': 'B', 'б': 'b',
#                  'В': 'V', 'в': 'v',
#                  'Г': 'G', 'г': 'g',
#                  'Д': 'D', 'д': 'd',
#                  'Е': 'Ye', 'е': 'ye',
#                  'Ж': 'Zh', 'ж': 'zh',
#                  'З': 'Z', 'з': 'z',
#                  'И': 'I', 'и': 'i',
#                  'Й': 'Y', 'й': 'y',
#                  'К': 'K', 'к': 'k',
#                  'Л': 'L', 'л': 'l',
#                  'М': 'M', 'м': 'm',
#                  'Н': 'N', 'н': 'n',
#                  'О': 'O', 'о': 'o',
#                  'П': 'P', 'п': 'p',
#                  'Р': 'R', 'р': 'r',
#                  'С': 'S', 'с': 's',
#                  'Т': 'T', 'т': 't',
#                  'У': 'U', 'у': 'u',
#                  'Ф': 'F', 'ф': 'f',
#                  'Х': 'Kh', 'х': 'kh',
#                  'Ц': 'Ts', 'ц': 'ts',
#                  'Ч': 'Ch', 'ч': 'ch',
#                  'Ш': 'Sh', 'ш': 'sh',
#                  'Щ': 'Shch', 'щ': 'shch',
#                  'Э': 'E', 'э': 'e',
#                  'Ю': 'Yu', 'ю': 'yu',
#                  'Я': 'Ya', 'я': 'ya',
#                  }
#
#
# def translit(langs, input_file, output_file):
#     in_text = open(input_file, 'r', encoding='utf-8').read()
#     if langs == ['ru', 'en']:
#         for key, value in translit_dict.items():
#             in_text = in_text.replace(key, value)
#     elif langs == ['en', 'ru']:
#         for key, value in translit_dict.items():
#             in_text = in_text.replace(value, key)
#     else:
#         print('Такие языки не поддерживаются данной программой!')
#     out_file = open(output_file, 'w', encoding='utf-8')
#     out_file.write(in_text)
#     out_file.close()
#
#
# input_file = input('Введите имя исходного файла: ')
# translit_langs = input('Введите, из какого в какой язык транслитерировать:\n'
#                        'Пример: en -> ru\n')
# output_file = input('Введите имя файла, в который сохранить перевод: ')
# translit(translit_langs.split(' -> '), input_file, output_file)

# 7.
# files = []


# while True:
#     file = input('enter the file name: ')
#     if file == 'quit':
#         break
#     files.append(file)
# with open('file.txt', 'w') as main:
#     for file in files:
#         try:
#             with open(file, 'r') as file_file:
#                 main.write(file_file.read())
#         except FileNotFoundError:
#             continue


# 8.
# def common_symbols():
#     files = []
#     while True:
#         file = input('enter the file name: ')
#         if file == 'quit':
#             break
#         files.append(file)
#
#     with open('file.txt', 'w') as main_w:
#         all_files = []
#         for file in files:
#             all_files.append(open(file, 'r'))
#         first = True
#         symbols = set()
#         for input_filename in all_files:
#             if first:
#                 symbols = set(input_filename.read())
#                 first = False
#             else:
#                 symbols = symbols.intersection(input_filename.read())
#         main_w.write(''.join(symbols))
#
#
# common_symbols()
