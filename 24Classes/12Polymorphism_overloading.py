class Person:
	""" Python doesn't have overloading, we use the *args
		to determine the quantity of arguments """
	def show_data(self, *args):
		if len(args) == 1:
			print(f'Hey my name\'s {args[0]}')
		elif len(args) == 2:
			print(f'Hey meu name\'s {args[0]} and I\'m {args[1]} years old')


def main():
	person = Person()
	person.show_data('Matheus')
	person.show_data('Matheus', 18)


if __name__ == '__main__':
	main()
