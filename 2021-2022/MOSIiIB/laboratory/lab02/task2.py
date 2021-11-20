import random
import math
from _collections import OrderedDict


def count_k(message):
    k = int(math.ceil((math.sqrt(len(message)) / 2)))
    while True:
        if len(message) == ((2 * k) ** 2):
            break
        else:
            message += random.choice('йцукенгшщзхъфыварлжэячсмитьбю')
    return k, message


def init_list(k):
    list_to_init = []
    counter = 0
    for i in range(k):
        temp_list = []
        for j in range(k):
            counter += 1
            temp_list.append(counter)
        list_to_init.append(temp_list)
    return list_to_init


def rotate_list(list):
    new_list = []
    for i, row in enumerate(list):
        temp_row_list = []
        for j, col in enumerate(row):
            temp_row_list.append(list[len(list) - j - 1][i])
        new_list.append(temp_row_list)
    return new_list


def init_big_table(list):
    not_rotated_list = list
    result_list = []
    rotated_list1 = rotate_list(not_rotated_list)
    rotated_list2 = rotate_list(rotated_list1)
    rotated_list3 = rotate_list(rotated_list2)
    for ix, item in enumerate(rotated_list1):
        temp_row = not_rotated_list[ix] + rotated_list1[ix]
        result_list.append(temp_row)
    for ix, item in enumerate(rotated_list2):
        temp_row = rotated_list3[ix] + rotated_list2[ix]
        result_list.append(temp_row)
    return result_list


def open_spaces(list, message):
    message_letters_left = message
    spaces = k ** 2
    i = 1
    while True:
        if i == spaces + 1:
            break
        rand_index_i = random.randint(0, (k * 2) - 1)
        rand_index_j = random.randint(0, (k * 2) - 1)
        if list[rand_index_i][rand_index_j] == i:
            list[rand_index_i][rand_index_j] = message_letters_left[0]
            message_letters_left = message_letters_left[1:]
            i += 1
    return message_letters_left


def sorted_to_string(res, password):
    res_dict = dict(zip(password, res))
    print("Зашифрованное сообщение в виде словаря до сортировки: ")
    print(res_dict)
    sorted_dict = sort_dict(res_dict)
    print("Зашифрованное сообщение в виде словаря после сортировки: ")
    print(sorted_dict)
    string_message = dict_to_string(sorted_dict)
    return string_message


def sort_dict(dict):
    return OrderedDict(sorted(dict.items()))


def dict_to_string(dict):
    new_message = ''
    for keys in dict:
        for key in keys:
            new_message += "".join(dict[key])
    return new_message


if __name__ == '__main__':
    message = input("Введите сообщение: ").replace(' ', '')

    k, message = count_k(message)

    print("Сообщение с учетом добавления произвольных символов: ")
    print(message)

    inited = init_list(k)

    print("Исходная матрица: ")
    print(*inited, sep="\n")

    res = init_big_table(inited)
    print("Образованная большая таблица k*2: ")
    print(*res, sep="\n")
    sliced_message = open_spaces(res, message)

    res = rotate_list(res)
    sliced_message = open_spaces(res, sliced_message)

    res = rotate_list(res)
    sliced_message = open_spaces(res, sliced_message)

    res = rotate_list(res)
    sliced_message = open_spaces(res, sliced_message)
    print("Зашифрованное сообщение в списковом представлении: ")
    print(*res, sep="\n", end="\n\n")

    password = input("Введите ключ (длина ключа = {}): ".format(len(res)))
    result = sorted_to_string(res, password)
    print("\n\nЗашифрованное сообщение: ")
    print(result)
