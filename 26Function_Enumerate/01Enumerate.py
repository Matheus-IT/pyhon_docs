a = ['nome', 'idade', 'sexo']
a = list(enumerate(a)) #Retorna pares de tuplas com (indice, valor)
print(a)

#Posso incrementar em um loop for:
for index, value in enumerate(['nome', 'idade', 'sexo']):
    print(f'Position {index} Value {value}')
