def ext_euclid(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, xx, yy = ext_euclid(b, a % b)
        x = yy
        y = xx - (a // b) * yy
        return d, x, y


def inverse(a, n):
    return ext_euclid(a, n)[1]


def xab(x, a, b, value):
    (G, H, P, Q) = value
    sub = x % 3

    if sub == 0:
        x = x * value[0] % value[2]
        a = (a + 1) % Q

    if sub == 1:
        x = x * value[1] % value[2]
        b = (b + 1) % value[2]

    if sub == 2:
        x = x * x % value[2]
        a = a * 2 % value[3]
        b = b * 2 % value[3]

    return x, a, b


def verify(g, h, p, x):
    return pow(g, x, p) == h


def pollard(G, H, P):
    Q = int((P - 1) // 2)

    x = G * H
    a = 1
    b = 1

    X = x
    A = a
    B = b

    for i in range(1, P):
        x, a, b = xab(x, a, b, (G, H, P, Q))

        X, A, B = xab(X, A, B, (G, H, P, Q))
        X, A, B = xab(X, A, B, (G, H, P, Q))

        if x == X:
            break

    nom = a - A
    denom = B - b

    res = (inverse(denom, Q) * nom) % Q

    if verify(G, H, P, res):
        return res

    return res + Q


if __name__ == '__main__':
    args = [(10, 64, 107)]
    for arg in args:
        res = pollard(*arg)
        print("{} ** {} ≡ {} (mod {})".format(arg[0], res, arg[1], arg[2]))
        print("Verify result: ", end="")
        if verify(arg[0], arg[1], arg[2], res):
            print("verified")
        else:
            print("not verified")
