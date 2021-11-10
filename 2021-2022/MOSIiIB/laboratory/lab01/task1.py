FIRST_SYMBOL_ACII = 97
LAST_SYMBOL_ACII = 122
alphabet = {"en": 26}
IGNORE_SYMBOLS = " 1234567890-=./[]';<>*-+|?,!"


def caesar(message, shift):
    new_message = ""
    for symbol in message:
        if symbol in IGNORE_SYMBOLS:
            new_message += symbol
            continue
        new_symbol = chr(FIRST_SYMBOL_ACII + ((ord(symbol) - FIRST_SYMBOL_ACII + shift) % alphabet["en"]))
        new_message += new_symbol
    return new_message


def atbash(message):
    new_message = ""
    for symbol in message:
        if symbol in IGNORE_SYMBOLS:
            new_message += symbol
            continue
        new_symbol = chr(FIRST_SYMBOL_ACII + LAST_SYMBOL_ACII - ord(symbol))
        new_message += new_symbol
    return new_message


if __name__ == '__main__':
    while (True):
        code = int(input(
            "Нажмите: \n\t1 - для работы с шифром цезаря;\n\t2 - для работы с шифром атбаш\n\t0 - для выхода из программы\n"))
        if (code == 1):
            message = input("Введите сообщение: ")
            shift = int(input("Задайте сдвиг (от 1 до 25): "))
            result = caesar(message, shift)
            print("\nЗашифрованное сообщение (Шифр Цезаря):\n{}".format(result))
        elif (code == 2):
            message = input("Введите сообщение: ")
            result = atbash(message)
            print("\nЗашифрованное сообщение (Шифр Атбаш):\n{}".format(result))
        elif (code == 0):
            break
        else:
            print("Ошибка ввода!")
