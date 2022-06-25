lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
#Tuplas são imutáveis
#lanche[1] = 'Refrigerante' <- ERRADO
print(lanche)
print()

for cont, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {cont}')
print()

for comida in range(0, 5):
    print(f'Eu comi {lanche[comida]} na posição {comida}')
print()

print('Comi pra caramba!!')
