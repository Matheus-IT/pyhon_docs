class Conta:
	_total_contas = 0

	def __init__(self, saldo=0.0):
		self._saldo = saldo
		Conta._total_contas += 1

	# To access a class attribute we have to have a static method
	# or a class method for the getter
	@staticmethod
	def get_total_contas() -> int:
		return Conta._total_contas


class Conta2:
	_total_contas = 0

	def __init__(self, saldo=0.0):
		self._saldo = saldo
		Conta2._total_contas += 1

	# To access a class attribute we have to have a static method
	# or a class method for the getter
	@classmethod
	def get_total_contas(cls):
		return cls._total_contas


c1 = Conta()
c2 = Conta()
c3 = Conta()
print(Conta.get_total_contas())

c4 = Conta2()
c5 = Conta2()
c6 = Conta2()
print(Conta.get_total_contas())

# No início pode parecer confuso qual usar: @staticmethod ou @classmethod?
# Isso não é trivial. Métodos de classe servem para definir um método que opera na classe,
# e não em instâncias. Já os métodos estáticos utilizamos quando não precisamos receber a
# referência de um objeto especial (seja da classe ou de uma instância) e funciona como
# uma função comum, sem relação. Classes podem ter filhas e aproveitar o código das
# classes mães. Um método de classe pode mudar a implementação, ou seja, pode ser reescrito
# pela classe filha. Já os métodos estáticos não podem ser reescritos pelas filhas, já que
# são imutáveis e não dependem de um referência especial.
