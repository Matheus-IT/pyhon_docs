def fatorial(num):
    fat = 1
    for cont in range(num, 0, -1):
        fat *= cont
    return fat


def dobro(num):
    return num * 2


def triplo(num):
    return num * 3


def raiz_quad(num):
    from math import sqrt
    return sqrt(num)
