#valores = list(range(4, 11)) #Uma lista com valores de 4 até 10

valores = [8, 2, 5, 4, 9, 3, 0] #Adicionar valores da forma tradicional
print(valores)

print('Valores ordem Crescente: ', end='')
valores.sort() #Organizar valores de forma crescente
print(valores)

print(f'Valores ordem Decrescente: ', end='')
valores.sort(reverse=True) #Organizar valores de forma decrescente
print(valores)

print('Colocar o número 7 na posição 4: ', end='')
valores.insert(3, 7) #Colocar o 7 na posição do 4
print(valores)

print('Eliminar o último valor da lista: ', end='')
valores.pop() #Eliminar o último valor de valores
print(valores)

print(f'Essa lista tem {len(valores)} elementos') #Mostra o comprimento de "valores"
