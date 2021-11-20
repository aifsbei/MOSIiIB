message = 'криптографиясерьезнаянаука'
password = 'математикаматематикаматема'
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'


def create_table(alphabet):
    alphabet_list = []
    current_row = alphabet
    alphabet_list.append(current_row)
    for item in alphabet:
        current_row = current_row[1:] + current_row[0]
        alphabet_list.append(current_row)
    alphabet_list.pop()
    return alphabet_list


def visioner(message, password, table):
    indexes_i = []
    res_string = ''
    for ix, letter in enumerate(message):
        index_i = table[0].find(letter)
        indexes_i.append(index_i)
    indexes_j = []
    for ix, letter in enumerate(password):
        index_j = table[0].find(letter)
        indexes_j.append(index_j)
    for i, row in enumerate(indexes_i):
        res_string += table[indexes_i[i]][indexes_j[i]]
    return res_string

def make_password(message, password):
    new_password = ''
    for ix, item in enumerate(message):
        new_password += password[ix % len(password)]
    print(new_password)
    return new_password

if __name__ == '__main__':
    message = input("Введите сообщение: ").replace(' ', '')
    print("Форматированное сообщение: ")
    print(message)
    print()
    password = input("Введите пароль (не превышающий длину сообщения): ")
    print("Дополненый ключ до длины сообщения: ")
    password = make_password(message, password)
    table = create_table(alphabet)
    print("\nТаблица: ")
    print(*table[0:3], sep='\n')
    print("...")
    print("...")
    print(*table[-3:], sep='\n')
    result = visioner(message, password, table)
    print("\nЗашифрованное сообщение: ")
    print(result)
