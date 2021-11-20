from _collections import OrderedDict
import random


def get_nm(message, password):
    n = len(password)
    result = len(message) / len(password)
    while True:
        if int(result) != result:
            message += random.choice('йцукенгшщзхъфыварлжэячсмитьбю')
            result = len(message) / len(password)
        else:
            break
    m = int(result)
    return n, m, message


def message_to_dict(message, m, n):
    message_dict = {}
    for i in range(n):
        temp_message = []
        for j in range(m):
            temp_message.append(message[i + j * n])
        message_dict[password[i]] = temp_message
    return message_dict


def sort_dict(dict):
    return OrderedDict(sorted(dict.items()))


def dict_to_string(dict):
    new_message = ''
    for keys in dict:
        for key in keys:
            new_message += "".join(dict[key])
    return new_message


if __name__ == '__main__':
    message = input("Введите сообщение: ").replace(" ", "")
    password = input("Введите пароль: ")
    n, m, message = get_nm(message, password)
    dict_message = message_to_dict(message, m, n)
    ordered_dict_message = sort_dict(dict_message)
    print("Зашифрованное сообщение: ")
    print(dict_to_string(ordered_dict_message))
