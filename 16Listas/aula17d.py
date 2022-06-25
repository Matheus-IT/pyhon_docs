a = [2, 3, 4, 7]
#b = a #Isso não é uma cópia, mas sim uma ligação
b = a[:] #Isso seria uma cópia dos valores
print('Antes: ')
print(f'Lista A: {a}')
print(f'Lista B: {b}')
b[2] = 8
print('Depois: ')
print(f'Lista A: {a}')
print(f'Lista B: {b}')
