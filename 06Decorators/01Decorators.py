# Na prática, o decorator é um mecanismo de sintaxe que chama uma função,
# passando outra como parâmetro, ou chama o construtor de uma classe,
# passando uma função como parâmetro. Pensando em alto nível, um decorator
# é uma informação declarativa sobre uma função em questão. Ele nos permite
# adicionar comportamentos extras a funções existentes, de forma declarativa.
# Isso é um recurso que pertence à meta programação.


def f1(func):
    def wrapper(*args, **kwargs):
        print('Started')
        func(*args, **kwargs)
        print('Ended')
    return wrapper


@f1
def f2(msg):
    print(msg)


f2('hello')
