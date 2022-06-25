class Conta:
	def __init__(self, saldo=0.0):
		self._saldo = saldo

	@property
	def saldo(self) -> float:
		return self._saldo

	@saldo.setter
	def saldo(self, saldo):
		if saldo < 0:
			print('Saldo não pode ser negativo')
		else:
			self._saldo = saldo


con = Conta(450)

print(con.saldo)
con.saldo = -50
con.saldo = 150
print(con.saldo)
