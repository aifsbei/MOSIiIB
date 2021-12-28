def algorithm1(u, v, n, b):
    j = n
    k = 0
    w = [None for i in range(j + 1)]
    while True:
        w[j] = (u[j - 1] + v[j - 1] + k) % b
        j = j - 1
        if j > 0:
            continue
        elif j == 0:
            w[0] = k
            break
    return w


def algorithm2(u, v, n, b):
    j = n
    k = 0
    w = [None for i in range(j)]
    while True:
        w[j - 1] = (u[j - 1] - v[j - 1] + k) % b
        j = j - 1
        if j > 0:
            continue
        elif j == 0:
            break
    return w


def algorithm3(u, v, b):
    m = len(v) - 1
    n = len(u) - 1
    w = [0 for i in range(n + m + 1)]
    j = m
    while True:
        if (v[j] == 0):
            w[j] = 0
        else:
            i = n
            k = 0
            while True:
                t = u[i] * v[j] + w[i + j] + k
                w[i + j] = t % b
                k = t / b
                i = i - 1
                if i > 0:
                    continue
                else:
                    w[j] = k
                    break
        j = j - 1
        if j > 0:
            continue
        elif j == 0:
            break
    return w


def algorithm4(u, v, b):
    t = 0
    m = len(v)
    n = len(u)
    w = [0 for i in range(n + m + 1)]
    for s in range(m + n):
        for i in range(s):
            t = t + (u[n - i - 1] * v[m - s + i - 1])
        w[m + n - s] = int(t % b)
        t = t / b
    return w


def algorithm5(u, v, b):
    n = len(u)
    t = len(v)
    q = [0 for j in range(n - t + 1)]
    while u >= v * (b ** (n - t)):
        q[n - t] += 1
        u = u - v * (b ** (n - t))
        for i in range(n, t + 1):
            if (u[i] >= v[t]):
                q[i - t - 1] = b - 1
            else:
                q[i - t - 1] = ((u[i] * b) + u[i - 1]) / v[t]
            while q[i - t - 1] * ((v[t] * b) + v[t - 1]) > u[i] * (b ** 2) + u[i - 1] * b + u[i - 2]:
                q[i - t - 1] -= 1
            u = u - q[i - t - 1] * (b ** (i - t - 1)) * v
            if u < 0:
                u = u + v * (b ** (i - t - 1))
                q[i - t - 1] -= 1
    r = u
    return q, r


if __name__ == '__main__':
    while True:
        try:
            result_code = int(input(
                """
Выберите алгоритм:
1 - Сложение неотрицательных целых чисел;
2 - Вычитание неотрицательных целых чисел;
3 - Умножение неотрицательных целых чисел столбиком;
4 - Быстрый столбик;
5 - Деление многоразрядных целых чисел
-------------------------
0 - Выход из программы
Введите номер операции: """
            ))
            if result_code > 5:
                print("Ошибка ввода!")
                continue
            if result_code == 0:
                break
        except:
            print("Ошибка ввода!")
            continue
        arr1 = input("Введите первое целое число: ")
        arr1 = list(arr1)
        arr2 = input("Введите второе целое число: ")
        arr2 = list(arr2)
        system = int(input("Введите систему счисления 2..16: "))
        arr1 = list(map(lambda x: int(x), arr1))
        arr2 = list(map(lambda x: int(x), arr2))

        if result_code == 1:
            print(algorithm1(arr1, arr2, len(arr1), system))

        if result_code == 2:
            print(algorithm2(arr1, arr2, len(arr1), system))

        if result_code == 3:
            print(algorithm3(arr1, arr2, system))

        if result_code == 4:
            print(algorithm4(arr1, arr2, system))

        if result_code == 5:
            print(algorithm5(arr1, arr2, system))
