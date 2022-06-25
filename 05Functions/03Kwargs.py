# No caso do **kwargs, os argumentos vem em forma de dicionário


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} - {value}')


print_info(name='Matheus', age=30, nacionality='Brasil')

