class Car:
	# class properties:
	counter = 0

	def __init__(self):
		Car.counter += 1

		# object properties:
		self.color = 'Black'
		self.seats = 7
		self.maximumSpeed = 200
		self.isTheEngineOn = False
		self.currentGear = 0
		self.gears = 7
		self.speed = 0

	# these are the methods:
	def turnOn(self):
		self.isTheEngineOn = True

	def turnOff(self):
		self.isTheEngineOn = False

	def speedUp(self):
		self.speed += 10

	def brake(self):
		self.speed -= 10

	def setGear(self, newGear):
		self.currentGear = newGear



''' Existem também funções específicas para manipulação de objetos de uma
determinada classe. São as funções abaixo:
● hasattr(objeto, propriedade) - Checa se um objeto possui uma determinada
propriedade;
● getattr(objeto, propriedade) - Retorna o valor de uma propriedade do
objeto;
● setattr(objeto, propriedade, valor) - Define o valor de uma propriedade do
objeto. Se esta propriedade não existe, ela é criada;
● delattr(objeto, propriedade) - Remove uma propriedade do objeto. '''

c1 = Car()
c2 = Car()
c3 = Car()
print(Car.counter)
