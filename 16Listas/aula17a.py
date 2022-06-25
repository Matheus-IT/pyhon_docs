lanche = ['Hamburger', 'Suco', 'Pizza', 'Pudim'] #Temos uma LISTA
print(lanche)
lanche[3] = 'Picolé' #As listas são mutáveis
print(lanche)
lanche.append('Cookie')
print(lanche)
lanche.insert(0, 'Cachorro-quente') #Adicionar um cachorro quente na posição 0
print(lanche)
#Como apagar ítens da lista:
#del lanche[3] #Apagar o ítem no índice 3 de lanche
#lanche.pop(3) #Apagar o ítem no índice 3 de lanche com o método pop
lanche.remove('Pizza') #Apagar o conteúdo de lanche 3, pizza
print(lanche)
