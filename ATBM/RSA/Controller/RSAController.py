from Model import DAO

x, y = 0, 1


def GCDExtended(a, b):
    global x, y

    if a == 0:
        x = 0
        y = 1
        return b
    gcd = GCDExtended(b % a, a)
    x1 = x
    y1 = y

    x = y1 - (b // a) * x1
    y = x1
    return gcd


def ModuloInverse(a, m):
    gcd = GCDExtended(a, m)
    inversed = x % m
    return inversed


def power_mod(a, b, mod):
    string_b = bin(b)[2:][::-1]
    array_a = [0 for _ in string_b]
    for i in range(len(string_b)):
        if i == 0:
            array_a[i] = a % mod
        else:
            array_a[i] = (array_a[i - 1] ** 2) % mod

    for i in range(len(string_b)):
        if string_b[i] == "0":
            array_a[i] = 1
        else:
            array_a[i] = array_a[i]

    temp = 1
    for i in array_a:
        temp *= i
        temp %= mod
    return temp


def Encrypt(k):
    text = int(DAO.GetDecText())
    return power_mod(text, k[1], k[0])


def Decrypt(k):
    crypt = int(DAO.GetDecCrypt())
    return power_mod(crypt, k[1], k[0])
