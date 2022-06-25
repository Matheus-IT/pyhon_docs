class Person():
    def __init__(self, name):
        self._name = name

    def other_name(self):
        return self._name

    @property
    def name(self):
        return self._name


col = Person('Name')
print(col.other_name)
print(col.name)

# O objetivo do decorator @property é criar um atributo artificial chamado
# name, que representa o acesso de leitura à variável _name. Repare
# que a implementação de name e de other_name são iguais, mas como
# other_name não está com o decorator @property, a referência para ela,
# sem o uso da sintaxe de chamada de função com (), faz com que uma instância
# do método seja retornada em vez de o método ser invocado. Com o
# decorator @property, a referência a col.name invoca o método name e,
# por isso, o retorno é o valor de _name.
