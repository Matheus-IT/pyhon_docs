# this is an informal interface
class Controller:
	# these are the abstract methods:
	def volume_up(self):
		pass

	def volume_down(self):
		pass

	def show_volume(self):
		pass


class RemoteControl(Controller):
	def __init__(self):
		self.__volume = 0

	def __get_volume(self):
		return self.__volume

	def __set_volume(self, val: int):
		self.__volume = val

	# these are the concrete implementations of the abstract methods
	def volume_up(self):
		if self.__get_volume() < 100:
			self.__set_volume(self.__get_volume() + 10)

	def volume_down(self):
		if self.__get_volume() > 0:
			self.__set_volume(self.__get_volume() - 10)

	def show_volume(self):
		print('Volume ', end='')
		for i in range(0, self.__get_volume(), 10):
			print('I', end='')
		print()


def main():
	c = RemoteControl()

	c.show_volume()
	for i in range(10):
		c.volume_up()
	c.show_volume()
	for i in range(5):
		c.volume_down()
	c.show_volume()

	# Such informal interfaces are fine for small projects where only a
	# few developers are working on the source code. However, as projects
	# get larger and teams grow, this could lead to developers spending
	# countless hours looking for hard-to-find logic errors in the codebase!


if __name__ == '__main__':
	main()
