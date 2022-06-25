# Definição de função
def soma(a2, b2): # Os parâmetros aqui precisam ter outro nome
    print(f'A = {a2} e B = {b2}')
    s = a2 + b2
    print(f'A soma vale A + B = {s}')


# Programa principal
a = int(input('Digite um valor para A: '))
b = int(input('Digite um valor para B: '))
soma(a, b)
