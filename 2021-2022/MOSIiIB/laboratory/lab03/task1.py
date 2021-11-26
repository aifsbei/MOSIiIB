alphabet = 'абвгдеёжзийклмнопрстуфкцчшщъыьэюя'
ignore_symbols = '!@#$%^&*(){}[]<>,./" '

def get_indexes(text):
    indexes = []
    for letter in text:
        try:
            indexes.append(alphabet.index(letter) + 1)
        except ValueError:
            indexes.append(ignore_symbols.index(letter) + 10000)
    return indexes


def format_gamma(gamma, message_length):
    new_gamma = ""
    for i in range(message_length):
        new_gamma += gamma[i % len(gamma)]
    return new_gamma


def encrypt(message_indexes, gamma_indexes):
    indexes = []
    for ix, item in enumerate(message_indexes):
        if message_indexes[ix] > 10000 or gamma_indexes[ix] > 10000:
            result = item
            indexes.append(result)
            continue
        result = (message_indexes[ix] + gamma_indexes[ix]) % len(alphabet)
        indexes.append(result)
    return indexes


def to_text(indexes):
    text = ""
    for index in indexes:
        if index > 10000:
            text += ignore_symbols[index - 10000]
            continue
        text += alphabet[index - 1]
    return text


if __name__ == '__main__':
    message = input("Введите сообщение: ")
    gamma = input("Введите ключ (гамма): ")
    new_gamma = format_gamma(gamma, len(message))
    print("\nПреобразование {} -> {}".format(gamma.upper(), new_gamma.upper()))
    message_indexes = get_indexes(message)
    print("\nВаше сообщение:\n{} ({})".format(message.upper(), message_indexes))
    gamma_indexes = get_indexes(new_gamma)
    print("\nВаша гамма:\n{} ({})".format(gamma.upper(), gamma_indexes))
    encrypted_message_indexes = encrypt(message_indexes, gamma_indexes)
    encrypted_message = to_text(encrypted_message_indexes)
    print("\nЗашифрованное сообщение:\n{} ({})".format(encrypted_message.upper(), encrypted_message_indexes))
