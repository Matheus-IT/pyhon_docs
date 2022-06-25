import abc


class Animal(abc.ABC):
	@abc.abstractmethod
	def eat(self):
		pass


class Chicken(Animal):
	def __init__(self):
		print(f'{__class__.__name__} created!')

	# overwriting the method eat of the super class
	def eat(self):
		print('Chicken eating')


class Cat(Animal):
	def __init__(self):
		print(f'{__class__.__name__} created!')

	# overwriting the method eat of the super class
	def eat(self):
		print('Cat eating')


def main():
	chicken = Chicken()
	cat = Cat()
	chicken.eat()
	cat.eat()


if __name__ == '__main__':
	main()
