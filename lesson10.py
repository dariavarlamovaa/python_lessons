# 'tic-tac-toe'
board = [['#', '#', '#'],
         ['#', '#', '#'],
         ['#', '#', '#']]
turn = 1


def check_win(board, symbol):
    if ((board[0][0] == board[0][1] == board[0][2] == symbol) or
            (board[1][0] == board[1][1] == board[1][2] == symbol) or
            (board[2][0] == board[2][1] == board[2][2] == symbol) or
            (board[0][0] == board[1][1] == board[2][2] == symbol) or
            (board[0][2] == board[1][1] == board[2][0] == symbol) or
            (board[0][0] == board[1][0] == board[2][0] == symbol) or
            (board[0][1] == board[1][1] == board[2][1] == symbol) or
            (board[0][2] == board[1][2] == board[2][2] == symbol)):
        return True
    return False


def make_turn(board, symbol):
    while True:
        try:
            row = int(input('введите номер ряда (1-3): '))
            col = int(input('введите номер столбца (1-3): '))
            if ((row in [1, 2, 3] and col in [1, 2, 3]) and
                    board[row - 1][col - 1] == '#'):
                break
            else:
                print('ошибка! неверный ввод.')
        except ValueError:
            pass
    board[row - 1][col - 1] = symbol


def tic_tac_toe(board, turn):
    if turn > 9:
        print('ничья')
        return
    symbol = 'X' if turn % 2 == 1 else 'О'
    print(f'ходят {symbol}. ход: {turn}')
    [print(*row, sep='\t') for row in board]
    make_turn(board, symbol)
    if check_win(board, symbol):
        print(f'победили {symbol}!')
        [print(*row, sep='\t') for row in board]
    else:
        tic_tac_toe(board, turn + 1)


tic_tac_toe(board, 1)


# import random

# def isPalindrome(x) -> bool:
#     x = str(x)
#     return True if x[::] == x[::-1] else False
#
# print(isPalindrome('-121'))

# def summa(a, b):
#     def check_ab(a, b):
#         return a > 0 and b > 0
#
#     if check_ab(a, b):
#         return a + b
#     return 'Wrong input'
#
#
# print(summa(2, -4))


# import random
# lst = [[random.randint(1,10) for i in range(2)] for j in range(4)]
# print(lst)
# lst.sort(key=lambda x: x[1])
# print(lst)


# def inf(x):
#     x + inf(lst)
#
#
# lst = [1]
# print(inf(lst))

# list_str = ['hello', 'python', 'abc']
# list_a = lambda strs: [x for x in strs if 'a' in x]
# print(list_a(list_str))
