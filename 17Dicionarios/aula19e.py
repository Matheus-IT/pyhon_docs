estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #Copia do dicionario 'estado' para lista 'brasil'

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
