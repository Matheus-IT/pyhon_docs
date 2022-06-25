inicio = int(input('Início contagem: '))
fim = int(input('Fim contagem: '))
passo = int(input('Passo: '))

for c in range(inicio, fim + 1, passo):
    print(c)
print('Fim')
