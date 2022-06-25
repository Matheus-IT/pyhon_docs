from time import sleep
valores = []
for cont in range(1, 6): #Ler vários valores pelo teclado e colocar na lista
    valores.append(int(input(f'Digite o {cont} valor: ')))

print('Vamos organizar os valores!')
valores.sort() #Organiza os valores em órdem crescente
sleep(2) #Gracinha que fiz pra ficar mais legal

print('Os valores são: ')
for c, val in enumerate(valores):
    print(f'Na posição {c} temos {val}')
print('A lista acabou!')
