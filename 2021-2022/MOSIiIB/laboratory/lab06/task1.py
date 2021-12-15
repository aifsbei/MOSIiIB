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


def pollard(n, c):
    a = c
    b = c
    while True:
        a = f(a, n) % n
        b = f(f(b, n), n) % n
        first = min(a - b, n)
        second = max(a - b, n)
        d = euclid(first, second)
        if d > 1 and d < n:
            p = d
            return p
        elif d == n:
            return -1
        elif d == 1:
            continue


def f(x, n):
    return (x ** 2) + 5 % n


if __name__ == '__main__':
    n = int(input("Введите число n: "))
    c = int(input("Введите число c: "))
    result = pollard(n, c)
    print("Нетривиальный делитель числа n = {}".format(result))
