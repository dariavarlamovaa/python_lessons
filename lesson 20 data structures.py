# СТРУКТУРЫ ДАННЫХ

# 1. Stack Data Structure
# class Stack:
#     def __init__(self, size, iterable: list | tuple | set = None):
#         self.lst = list(iterable[:size]) if iterable else []
#         self.size = size
#
#     def push(self, value):
#         if not self.is_full():
#             return self.lst.append(value)
#         else:
#             return 'Stack is full'
#
#     def is_full(self):
#         return len(self.lst) == self.size
#
#     def is_empty(self):
#         if len(self.lst) == 0:
#             return 'Stack is empty!'
#         return False
#
#     def pop(self):
#         return self.is_empty() or self.lst.pop()
#
#     def peek(self):
#         return self.is_empty() or self.lst[-1]
#
#     def size(self):
#         return len(self.lst)
#
#     def __str__(self):
#         return ' -> '.join(map(str, self.lst))
#
#
# a = Stack(3, [1, 2, 3, 4, 5])
# print(a.peek())
# print(a.pop())
# a.push(5)
# a.push(0)
# print(a.is_full())
# print(a)

# --------------stack example---------------
# string = input('enter the string: ')
# stack = []
# is_good = True
#
# for symbol in string:
#     if symbol in '([{':
#         stack.append(symbol)
#     elif symbol in ')]}':
#         if not stack:
#             is_good = False
#             break
#         open_bracket = stack.pop()
#         if open_bracket == '(' and symbol == ')':
#             continue
#         if open_bracket == '[' and symbol == ']':
#             continue
#         if open_bracket == '{' and symbol == '}':
#             continue
#         is_good = False
#         break
# if is_good and len(stack) == 0:
#     print('yes')
# else:
#     print('no')

# 2. Singly Linked List
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next  # ссылка на следующую ноду
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self, value):
#         new_node = Node(value)
#
#         # если список пустой, делаем новую ноду головой
#         if self.head is None:
#             self.head = new_node
#             return
#
#         # если список не пустой, перебираем все ноды, пока
#         # не дойдем до последней
#         current_node = self.head
#         while current_node.next is not None:
#             current_node = current_node.next
#
#         # добавляет нашу ноду в next последней, делая ее новой последней
#         current_node.next = new_node
#
#     def delete(self, value):
#         # если список пустой, ничего не делаем
#         if self.head is None:
#             return
#         # если то, что мы хотим удалить, это голова, то удаляем ее
#         if self.head.value == value:
#             self.head = self.head.next
#             return
#
#         # если список не пустой, перебираем все ноды, пока
#         # не дойдем до искомого value или до конца
#         current_node = self.head
#         while current_node.next is not None:
#             if current_node.next.value == value:
#                 current_node.next = current_node.next.next
#                 return
#             current_node = current_node.next
#
#     def show(self):
#         # если список пустой, выводим сообщение об этом
#         if self.head is None:
#             print('List is empty!')
#             return
#
#         # если список не пустой, перебираем и выводим все ноды
#         current_node = self.head
#         while current_node is not None:
#             print(current_node.value, end=' -> ')
#             current_node = current_node.next
#         print('None')
#
#
# a = LinkedList()
# a.append(5)
# a.append(4)
# a.append(3)
# a.append(2)
# a.append(1)
# a.show()

# 3. Двухсвязный список
# class Node:
#     def __init__(self, value, prev=None, next=None):
#         self.value = value
#         self.prev = prev
#         self.next = next  # ссылка на следующую ноду
#
#
# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self, value):
#         new_node = Node(value)
#
#         # если список пустой, делаем новую ноду головой
#         if self.head is None:
#             self.head = new_node
#             return
#
#         # если список не пустой, перебираем все ноды, пока
#         # не дойдем до последней
#         current_node = self.head
#         while current_node.next is not None:
#             current_node = current_node.next
#
#         # добавляет нашу ноду в next последней, делая ее новой последней
#         current_node.next = new_node
#         new_node.prev = current_node
#
#     def delete(self, value):
#         # если список пустой, ничего не делаем
#         if self.head is None:
#             return
#         # если то, что мы хотим удалить, это голова, то удаляем ее
#         if self.head.value == value:
#             self.head = self.head.next
#             if self.head is not None:
#                 self.head.prev = None
#             return
#
#         # если список не пустой, перебираем все ноды, пока
#         # не дойдем до искомого value или до конца
#         current_node = self.head
#         while current_node.next is not None:
#             if current_node.next.value == value:
#                 current_node.next = current_node.next.next
#                 if current_node.next is not None:
#                     current_node.next.prev = current_node
#                 return
#             current_node = current_node.next
#
#     def show(self):
#         # если список пустой, выводим сообщение об этом
#         if self.head is None:
#             print('List is empty!')
#             return
#
#         # если список не пустой, перебираем и выводим все ноды
#         current_node = self.head
#         while current_node is not None:
#             print(current_node.value, end=' <-> ')
#             current_node = current_node.next
#         print('None')
#
#
# a = DoublyLinkedList()
# a.append(5)
# a.append(4)
# a.append(2)
# a.append(3)
# a.delete(4)
# a.show()


# 4. Очередь
# class Queue:
#     def __init__(self, size):
#         self.lst = []
#         self.size = size
#
#     def is_empty(self):
#         return len(self.lst) == 0
#
#     def is_full(self):
#         return len(self.lst) == self.size
#
#     def enqueue(self, value):
#         if len(self.lst) >= self.size:
#             return 'Queue is full!'
#         self.lst.append(value)
#
#     def dequeue(self):
#         return self.lst.pop(0)
#
#     def show(self):
#         print(f' <- '.join(map(str, self.lst)))
#
#
# a = Queue(5)
# a.enqueue(3)
# a.enqueue(1)
# a.enqueue(2)
# a.enqueue(4)
# a.show()
# print(a.dequeue())
# a.show()
# a.enqueue(10)
# a.enqueue(11)
# a.enqueue(90)
# a.show()


# 5. Очередь с приоритетом
# class PriorityQueue(Queue):
#     def prior_insert(self, value):
#         if len(self.lst) >= self.size:
#             return 'Queue is full'
#         priority = value[1]
#         for i in range(len(self.lst)):
#             if priority > self.lst[i][1]:
#                 self.lst.insert(i, value)
#                 break
#         else:
#             self.lst.append(value)
#
#     def peek(self):
#         return self.lst[0][0]
#
#
# q = PriorityQueue(3)
# q.prior_insert(('Помыть посуду', 7))
# q.prior_insert(('Погулять с друзьями', 4))
# q.prior_insert(('Сделать дз', 10))
# q.prior_insert(('Посмотреть фильм', 3))
# q.show()
# print(q.peek())
# print(q.dequeue())
# q.show()
