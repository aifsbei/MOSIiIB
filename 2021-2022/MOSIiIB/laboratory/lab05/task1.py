import random


def fermat(n):
    a = random.randint(2, n - 2)
    r = a ** (n - 1) % n
    return r == 1


def jacoby(a, n):
    if (a == 0):
        return 0
    result = 1
    if (a < 0):
        a = -a
        if (n % 4 == 3):
            result = -result
    if (a == 1):
        return result
    while (a):
        if (a < 0):
            a = -a
            if (n % 4 == 3):
                result = -result
        while (a % 2 == 0):
            a = a // 2
            if (n % 8 == 3 or n % 8 == 5):
                result = -result
        a, n = n, a
        if (a % 4 == 3 and n % 4 == 3):
            result = -result
        a = a % n
        if (a > (n // 2)):
            a = a - n
    if (n == 1):
        return result
    return 0


def solovay_strassen(n):
    a = random.randint(2, n - 2)
    r = a ** ((n - 1) / 2)
    if (r != 1 and r != (n - 1)):
        return False
    s = jacoby(a, n)
    return not ((r - s) % n == 0)


def miller_rabin(n):
    a = random.randint(2, n - 2)
    d = n - 1
    s = 0
    while (d % 2 == 0):
        s = s + 1
        d = int(d / 2)
    x = a ** d
    x = x % n
    if (x == 1 or x == (n - 1)):
        return True
    r = 1
    while (r < (s - 1)):
        x = x ** 2
        x = x % n
        if (x == 1):
            return False
        if (x == (n - 1)):
            return True
    return False


if __name__ == '__main__':
    while True:
        try:
            result_code = int(input(
                """
Выберите алгоритм проверки числа на простоту
    1 - Алгоритм Ферма;
    2 - Алгоритм Соловэя-Штрассена;
    3 - Алгоритм Миллера-Рабина;
    -------------------------
    0 - Выход из программы
Введите номер операции: """
            ))
            if result_code > 3:
                print("Ошибка ввода!")
                continue
            if result_code == 0:
                break
        except:
            print("Ошибка ввода!")
            continue

        try:
            n = int(input("Введите нечетное целое число > 5: "))
        except:
            print("Ошибка ввода!")
            continue

        result = False

        if result_code == 1:
            result = fermat(n)

        if result_code == 2:
            result = solovay_strassen(n)

        if result_code == 3:
            result = miller_rabin(n)

        if result:
            print("Число {}, вероятно, простое".format(n))
        else:
            print("Число {} составное".format(n))
