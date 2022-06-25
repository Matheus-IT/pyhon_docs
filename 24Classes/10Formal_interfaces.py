import abc


# abstract base classes
class Bird(abc.ABC):
	@abc.abstractmethod
	def fly(self):
		pass


class Parrot(Bird):
	def fly(self):
		print('Flying!')


class Aeroplane(abc.ABC):
	@abc.abstractmethod
	def fly(self):
		pass


class Boeing(Aeroplane):
	def fly(self):
		print('Fooshhhuuu...')


def main():
	p = Parrot()
	b = Boeing()

	p.fly()
	b.fly()
	print(isinstance(p, Bird))
	print(isinstance(b, Aeroplane))


if __name__ == '__main__':
	main()
