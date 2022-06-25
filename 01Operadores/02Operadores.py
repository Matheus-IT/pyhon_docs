#nome = str(input('Qual é o seu nome? '))
#print('Prazer em te conhecer {:=^20}'.format(nome))
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
s = n1 + n2
m = n1 * n2
d = n1 * n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {}, a divisão é {:.2f}'.format(s, m, d), end=' ')
print('A divisão inteira é {}, potência {}'.format(di, e))
