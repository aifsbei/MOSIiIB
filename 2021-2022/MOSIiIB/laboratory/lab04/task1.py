def euclid(a, b):
    r = []
    r.append(a)
    r.append(b)
    i = 1
    while True:
        r.append(r[i - 1] % r[i])
        if r[i + 1] == 0:
            d = r[i]
            return d
        else:
            i = i + 1


def binary_euclid(a, b):
    g = 1
    while a % 2 == 0 and b % 2 == 0:
        a = a / 2
        b = b / 2
        g = 2 * g
    u = a
    v = b
    while u != 0:
        while u % 2 == 0:
            u = u / 2
        while v % 2 == 0:
            v = v / 2
        if u >= v:
            u = u - v
        else:
            v = v - u
    d = g * v
    return d


def extended_euclid(a, b):
    r = []
    x = []
    y = []

    r.append(a)
    r.append(b)

    x.append(1)
    x.append(0)

    y.append(0)
    y.append(1)

    while r[1] != 0:
        q = r[0] // r[1]
        r[0], r[1] = r[1], r[0] - (r[1] * q)
        x[0], x[1] = x[1], x[0] - (x[1] * q)
        y[0], y[1] = y[1], y[0] - (y[1] * q)

    d, x, y = r[0], x[0], y[0]

    return d, x, y


def binary_extended_euclid(a, b):
    g = 1

    while a % 2 == 0 and b % 2 == 0:
        a = a / 2
        b = b / 2
        g = 2 * g

    u = a
    v = b

    A = 1
    B = 0
    C = 0
    D = 1

    while u != 0:

        while u % 2 == 0:

            u = u / 2

            if A % 2 == 0 and B % 2 == 0:
                A = A / 2
                B = B / 2
            else:
                A = (A + B) / 2
                B = (B - A) / 2

        while v % 2 == 0:
            v = v / 2

            if C % 2 == 0 and D % 2 == 0:
                C = C / 2
                D = D / 2
            else:
                C = (C + B) / 2
                D = (D - A) / 2

        if u >= v:
            u = u - v
            A = A - C
            B = B - D
        else:
            v = v - u
            C = C - A
            D = D - B

    d = g * v
    x = C
    y = D

    return d, x, y


if __name__ == '__main__':
    while True:
        try:
            result_code = int(input(
                """
Выберите алгоритм нахождения НОД:
    1 - Алгоритм Евклида;
    2 - Бинарный алгоритм Евклида;
    3 - Расширенный алгоритм Евклида;
    4 - Расширенный бинарный алгоритм Евклида;
    -------------------------
    0 - Выход из программы
Введите номер операции: """
            ))
            if result_code > 4:
                print("Ошибка ввода!")
                continue
            if result_code == 0:
                break
        except:
            print("Ошибка ввода!")
            continue

        first = int(input("Введите первое число: "))
        second = int(input("Введите второе число: "))
        if first < second:
            first, second = second, first
        print(
            """
Ваши числа:
    a = {}
    b = {}
""".format(first, second))

        if result_code == 1:
            gcd = euclid(first, second)
            print("НОД для {} и {} = {}".format(first, second, gcd))

        if result_code == 2:
            gcd = binary_euclid(first, second)
            print("НОД для {} и {} = {}".format(first, second, gcd))

        if result_code == 3:
            gcd, x, y = extended_euclid(first, second)
            print("НОД для {} и {} = {}\nx = {}\ny = {}\n\n{}*{} + {}*{} = {}"
                  .format(first, second, gcd, x, y, first, x, second, y, gcd))

        if result_code == 4:
            gcd, x, y = binary_extended_euclid(first, second)
            print("НОД для {} и {} = {}\nx = {}\ny = {}\n\n{}*{} + {}*{} = {}"
                  .format(first, second, gcd, x, y, first, x, second, y, gcd))
