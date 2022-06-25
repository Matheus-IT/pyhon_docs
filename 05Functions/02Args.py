# Existe uma forma no Python de definir as funções para que recebam uma
# quantidade variável de argumentos, além da forma normal de definição de
# argumentos.


def print_all_3times(*args):
    for parameter in args:
        print(f'{parameter}! {parameter}! {parameter}!')


print_all_3times("Olá", "Python", "Matheus")
