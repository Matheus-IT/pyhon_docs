class Conta:
    # __slots__ pode guardar uma lista de atributos da classe definidos por nós:
    __slots__ = ['_numero', '_titular', '_saldo', '_limite']

    def __init__(self, numero, titular, saldo, limite=1000.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite


conta = Conta(12345, 'nome_titular', 1000, 10000)
# Agora, quando tentamos adicionar um atributo na classe recebemos um erro:
setattr(conta, nome, 'fulano') # this will end up in an error
