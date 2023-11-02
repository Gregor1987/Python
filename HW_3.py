# # def list_sort(some_list):
# #     for i in range(len(some_list)):
# #         for j in range(len(some_list) - 1):
# #             if some_list[j] > some_list[j + 1]:
# #                 some_list[j], some_list[j + 1] = some_list[j + 1], some_list[j]
# #     return some_list
# #
# #
# # unsorted_list = [1, 7, 5, 9, 12, 5, 48, 6]
# # print(list_sort(unsorted_list))
# # from decimal import Decimal
# #
# #
# # def premium(list_names, list_salaries, list_premiums):
# #     # for i in range(len(list_premiums)):
# #     #     list_premiums[i].replace('%', '')
# #     payments = {}
# #     for i in range(len(list_names)):
# #         payments[list_names[i]] = round(Decimal(list_salaries[i] * (float(list_premiums[i].replace('%', ''))/100)), 2)
# #     return payments
# #
# #
# # list_names = ['Ivan', 'Alex', 'Juhn']
# # list_salaries = [100, 120, 50]
# # list_premiums = ['10.25%', '15.65%', '5.25%']
# #
# # for name, award in premium(list_names, list_salaries, list_premiums).items():
# #     print(f'{name} => {award}')
#
# # def sum_of_nums(list_nums, ind1, ind2):
# #     result = 0
# #     if ind1 > ind2:
# #         ind1, ind2 = ind2, ind1
# #     if ind1 < 0:
# #         ind1 = 0
# #     if ind2 > len(list_nums) - 1:
# #         ind2 = len(list_nums) - 1
# #     for i in list_nums[ind1 + 1: ind2 - 1]:
# #         result += i
# #     return result
# #
# #
# # num1 = int(input('ind1: '))
# # num2 = int(input('ind2: '))
# # list_of_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # print(sum_of_nums(list_of_nums, num1, num2))
#
# # def balance(some_dict):
# #     fin_result = {}
# #     # check = True
# #     for key, value in some_dict.items():
# #         fin_result[key] = sum(value)
# #         # if fin_result[key] < 0:
# #             # check = False
# #     return fin_result, all(value if value > 0 else 0 for value in fin_result.values())
# #
# #
# # some_dict = {'comp1': [5000, 1000, -3000],
# #              'comp2': [2000, -1000, 7000],
# #              'comp3': [1000, -6000, 3000]}
# #
# # print(balance(some_dict))
#
# # def transpone(matrix):
# #     new_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
# #     for i in range(len(matrix)):
# #         # new_matrix[i] = []
# #         for j in range(len(matrix[0])):
# #             new_matrix[j][i] = matrix[i][j]
# #     return new_matrix
# #
# #
# # matrix = [[1, 2, 3], [3, 2, 1]]
# # print(transpone(matrix))
# #
# # def reverse(**kwargs):
# #     result_dict = {}
# #     for k, v in kwargs.items():
# #         if type(v) == dict or \
# #                 type(v) == list or \
# #                 type(v) == set or \
# #                 type(v) == tuple or \
# #                 type(v) == frozenset:
# #             v = str(v)
# #         result_dict[v] = k
# #     return result_dict
# #
# #
# # print(reverse(a='jlby', b='ldf', c=3, d=[1, 2, 3]))
#
# def operation():
#     oper = input(f'выберите действие:\nа - внести\nw - снять\ne - выйти\n')
#     return oper
#
#
# def add(amount):
#     global account
#     global count
#     if account > 5_000_000:
#         account -= amount * 0.1
#     while amount % 50 != 0:
#         amount = int(input('incorrect amount, try again: '))
#     account += amount
#     count += 1
#     if count % 3 == 0:
#         account *= 1.03
#     return account
#
#
# def withdraw(amount):
#     global account
#     global count
#     if account > 5_000_000:
#         account -= amount * 0.1
#     while amount % 50 != 0 or amount > account:
#         amount = int(input('incorrect amount, try again: '))
#     commission = amount * 0.015
#     if commission < 30:
#         commission = 30
#     elif commission > 600:
#         commission = 600
#     account -= (amount + commission)
#     count += 1
#     if count % 3 == 0:
#         account *= 1.03
#     return account
#
#
# account = 0
# count = 0
# oper = operation()
# while oper != 'e':
#     if oper == 'a':
#         print(add(int(input('введите сумму: '))))
#         oper = operation()
#     elif oper == 'w':
#         print(withdraw(int(input('введите сумму: '))))
#         oper = operation()
#     else:
#         print('incorrect input, try again')
#         oper = operation()
# if oper == 'e':
#     print('goodbye')


# a, b, c, *d = input().split('/')
# some_dict = {b: a, c: tuple(d)}
# print(some_dict)
#
# some_text = 'asdfkjhvzjxnvl'
# some_dict = {i: ord(i) for i in some_text}
# print(some_dict)
# some_dict_iter = iter(some_dict.items())
# print(next(some_dict_iter))
# print(next(some_dict_iter))
# print(next(some_dict_iter))
# print(next(some_dict_iter))
# print(next(some_dict_iter))
#
# some_list = [i for i in range(101) if i % 2 == 0]
# print([i for i in range(101) if i % 2 == 0 and sum(map(int, str(i))) != 8])

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)

# gen = (
#     ("FizzBuzz" if i % 5 == 0 and i % 3 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i)
#     for i in range(1, 101))
# for i in range(100):
#     print(next(gen))
#

# some_gen = (f'{i} * {j} = {i * j}' for i in range(2, 11) for j in range(2, 11))
# for i in range(100):
#     print(next(some_gen))

# def simple_nums(n):
#     for i in range(2, n):
#         check = False
#         for j in range(2, int(i ** 0.5) + 1):
#             if i % j == 0:
#                 check = True
#                 break
#         if not check:
#             yield i
#
#
# num = int(input("input number: "))
# some_func = simple_nums(num)
# for k in range(1000):
#     print(next(some_func))
import random as rnd


def chess_board(board):
    # board = [[0 for i in range(8)] for j in range(8)]
    # count = 0
    # while count < 8:
    #     state = rnd.getstate()
    #     if board[rnd.randint(0, len(board) - 1)][rnd.randint(0, len(board[0]) - 1)] == 0:
    #         rnd.setstate(state)
    #         board[rnd.randint(0, len(board) - 1)][rnd.randint(0, len(board[0]) - 1)] = 1
    #         count += 1
    # print(*board, sep='\n')
    check = True
    for i in range(len(board)):
        if sum(board[i]) > 1:
            check = False
            break

    for i in range(len(board[0])):
        summ = 0
        for j in range(len(board[0])):
            summ += board[j][i]
        if summ > 1:
            check = False
            break

    return board, check


count = 0
while count < 4:
    board = [[0 for i in range(8)] for j in range(8)]
    board_count = 0
    while board_count < 8:
        state = rnd.getstate()
        if board[rnd.randint(0, len(board) - 1)][rnd.randint(0, len(board[0]) - 1)] == 0:
            rnd.setstate(state)
            board[rnd.randint(0, len(board) - 1)][rnd.randint(0, len(board[0]) - 1)] = 1
            board_count += 1
    a, b = chess_board(board)
    if b:
        print(*a, sep='\n')
        count += 1
        print()
