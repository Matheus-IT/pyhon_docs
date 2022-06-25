class Caneta():
	def __init__(self):
		self._modelo: str = ''
		self._cor: str = ''
		self._tampa: bool = False

	def get_modelo(self) -> str:
		return self._modelo

	def set_modelo(self, modelo: str):
		self._modelo = modelo


c = Caneta()
c.set_modelo('bic cristal')
print(c.get_modelo())
