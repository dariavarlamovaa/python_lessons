# GIL - Global Interpreter Lock


# import multiprocessing
# import random
# import time

# def get_name():
#     time.sleep(3)
#     name = multiprocessing.current_process().name
#     print(multiprocessing.current_process().pid)
#     print(f'Process {name} ended')
#
#
# if __name__ == '__main__':
#     print(multiprocessing.cpu_count())
#     pr = multiprocessing.Process(target=get_name, name='First')
#     pr2 = multiprocessing.Process(target=get_name, name='Second')
#     pr.start()
#     pr.join()
#     pr2.start()


# task 1
# def get_max(nums):
#     print(max(nums))
#
#
# def get_min(nums):
#     print(min(nums))
#
#
# if __name__ == '__main__':
#     nums = map(int, input('enter the numbers, comma separated: ').strip().split(','))
#     pr = multiprocessing.Process(target=get_max, args=(nums,))
#     pr2 = multiprocessing.Process(target=get_min, args=(nums,))
#     pr.start()
#     pr.join()
#     pr2.start()


# -------------------------------------------
# Locker - блокирует доступ остальных процессов
# Release - наоборот


# def lock_process(locker):
#     locker.acquire()
#     print(multiprocessing.current_process().name)
#     locker.release()
#
#
# if __name__ == '__main__':
#     locker = multiprocessing.Lock()
#     for i in range(3):
#         pr = multiprocessing.Process(target=lock_process, args=(locker,))
#         pr.start()
#     time.sleep(3)


# ---------------------------------------------

# def get_name(n):
#     name = multiprocessing.current_process().name
#     print(f'Process {name} in work')
#     time.sleep(2)
#     print(multiprocessing.current_process().pid, 'finished')
#     return name
#
#
# if __name__ == '__main__':
#     count = multiprocessing.cpu_count()
#     with multiprocessing.Pool(count) as p:
#         res = p.map(get_name, range(16))
#         p.close()
#         p.join()
#         print(res)


# task 2 -------- распаралелить нахождение суммы списка

# def end():
#     print('Process is finished')
#
#
# def sum_sum(lst):
#     return sum(lst)
#
#
# if __name__ == '__main__':
#     count = multiprocessing.cpu_count()
#     nums = [random.randint(-10, 10) for i in range(100)]
#     nums = [nums[i:i + 20] for i in range(0, 41, 10)]
#     with multiprocessing.Pool(count) as p:
#         res = p.map_async(sum_sum, nums, callback=end)
#         p.close()
#         for row in nums:
#             print(row, sum(row))


# my tasks

# 1.
# def square(n):
#     print(f'square is 1111 for {n}')
#
#
# def circle(n):
#     print(f'square is 2222 for {n}')
#
#
# if __name__ == '__main__':
#     pr1 = multiprocessing.Process(target=square, args=(2, ))
#     pr1.start()
#
#     pr2 = multiprocessing.Process(target=circle, args=(5, ))
#     pr2.start()
#
#     pr1.join()
#     pr2.join()
#     print(multiprocessing.cpu_count())


# 2.

# fruits = ['Apple', 'Orange', 'Guava', 'Papaya', 'Banana']
# count = 1
# queue = multiprocessing.Queue()
# print('pushing items to the queue:')
# for fr in fruits:
#     print('item no: ', count, ' ', fr)
#     queue.put(fr)
#     count += 1
#
# print('\npopping items from the queue:')
# count = 0
# while not queue.empty():
#     print('item no: ', count, ' ', queue.get())
#     count += 1
