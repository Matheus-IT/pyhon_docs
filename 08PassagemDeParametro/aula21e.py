def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


print(f'O resultado é: {fatorial(int(input("Digite um valor: ")))}')
