''' A função “ update() ” recebe um dicionário como parâmetro e insere os
    pares deste dicionário parâmetro no dicionário através do qual a função é
    chamada. Caso existam chaves coincidentes, o primeiro dicionário é
    atualizado com os valores do dicionário passado como parâmetro
'''

aluno_original = {"nome": "José", "idade": 20, "nota": 9.2}
aluno_update = {"peso": 75, "nota": 8.7}
aluno_original.update(aluno_update)
print(aluno_original)
