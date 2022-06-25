''' A função “ get() ” é muito útil para evitar erros de chave inexistente. Ela
    recebe dois parâmetros, que são a chave a ser buscada e um valor de
    retorno. Ela retorna o valor de desta chave se ela existir no dicionário, e se
    não existir, retorna aquilo que definimos como valor de retorno, ou None se
    nenhum valor de retorno for definido
'''

aluno = {"nome": "José", "idade": 20, "nota": 9.2}
print(aluno.get("nome"))
print(aluno.get("peso"))
print(aluno.get("peso", "Não existe"))
