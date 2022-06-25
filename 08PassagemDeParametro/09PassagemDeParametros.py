def dobro(num):
    num *= 2
    return num


def dobro_R(val):
    val[0] *= 2
    return val


n = int(input(' - Digite um numero: '))
print(f' - Valor de num: {dobro(n)}') #'N' vai como valor
print(f' - Valor de n: {n}')
v = [int(input(' - Digite um numero: '))]
print(f' - valor de val: {dobro_R(v)}') #'V' vai como "referencia"
print(f' - Valor de v: {v}')
