from math import sqrt, ceil, floor

num = int(input('Digite um número: '))
raiz = sqrt(num)
#Arredondar para cima:
print('A raiz quadrada de {} arredondada pra cima {}'.format(num, ceil(raiz)))

#Arredondar para baixo:
print('A raiz quadrada de {} arredondada pra baixo {}'.format(num, floor(raiz)))

print('A raiz quadrada de {} é igual a {}'.format(num, raiz))
