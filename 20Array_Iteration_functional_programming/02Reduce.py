from functools import reduce #tem de ser importada de functools

def soma(n1, n2):
    return n1 + n2


l = [47, 11, 42, 13]
#Vai retornar a soma de todos os elementos da lista 'l'
s = reduce(soma, l) #Posso colocar um valor inicial também
print(s)
