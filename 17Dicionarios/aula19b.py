filme = {'título': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}
print(filme.values()) #Mostra APENAS OS VALORES
print(filme.keys()) #Mostra APENAS AS CHAVES
for k, v in filme.items(): #Mostra os dois
    print(f'O {k} é {v}')
