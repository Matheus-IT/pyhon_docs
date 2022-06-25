def teste(b):
    global a
    a = 8 #Modifica o valor da variavel global
    b += 4
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')


a = 5
teste(a)
print(f'A fora vale {a}')
#print(f'B fora vale {b}') -> Nao existe b fora da funcao
