# Na prática, a função geradora permite que ela retorne um elemento e,
# quando for chamada novamente, consiga restaurar o estado de execução anterior
# e retornar um novo elemento.


def simple_generator():
    yield 1
    yield 2
    yield 3


for val in simple_generator():
    print(val)

# A função geradora “gera” um valor toda vez que é “chamada” e, aqui,
# usamos aspas, pois não é uma chamada comum. Por padrão, as funções
# geradoras podem ser iteradas no comando for, que já sabe como obter
# os novos valores gerados por ela.
# No nosso programa isso é muito útil, pois, para percorrermos todos os
# dados dos arquivos, não precisamos criar nenhuma lista com eles em memória.


def simple_generator2():
    for x in range(10):
        yield x


print()
for val in simple_generator2():
    print(val)

# Para obter os valores gerados, usamos a função
# next(generator_function). Esta é que faz com que a função geradora
# seja executada, gere um elemento e tenha seu estado preservado, até
# que outra chamada com next() seja feita


def simple_generator3(x):
    for v in range(x):
        yield v


print()
my_generator = simple_generator3(2)
print(next(my_generator))
print(next(my_generator))
# print(next(my_generator)) # Not going to show

# Além disso, existem as expressões geradores,que têm sintaxe semelhante às
# list comprehensions,mas não criam listas em memória
my_generator = (x for x in range(10))
print()
for val in my_generator:
    print(val)
