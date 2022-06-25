a = [1, 2, 3]
b = [4, 5, 6]
c = list(zip(a, b)) # Retorna objeto zip com tuplas dos pares
print(c)

# Podemos trabalhar com dicionários também:
person1 = {'a':'Matheus', 'b':18}
person2 = {'c':'Carol', 'd':20}
person3 = list(zip(person1, person2.values())) # Same as zip(person1.keys(), person2.values())
print(person3)

# Podemos usar zip para 'criar indices':
index = ['nome', 'idade', 'sexo']
value = ['Matheus', 18, 'M']
person4 = zip(index, value)
for k, v in person4:
    print(f'{k}:{v}')
