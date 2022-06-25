def add(x, y):
    return x + y


def times(func, x, y):
    return func(x, y)


a = 2
b = 4
r = times(add, a, b)
print(' - Resultado = ', r)
