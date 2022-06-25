class Car:
    def __init__(self):
        self.color = 'Black'
        self.seats = 7
        self.maximum_speed = 200
        self.on = False

    def set_on(self, option: bool):
        self.on = option


# this class inherits from Car
class Gol(Car):
    def __init__(self):
        # here he call the constructor of 'Car'
        Car.__init__(self)
        # super().__init__() # you can also write this way, for superclasses

        self.color = 'Silver'
        self.seats = 5
        self.air_conditioner_on = False

    def set_air_conditioner_on(self, option: bool):
        self.air_conditioner_on = option


carro_gol = Gol()
print(carro_gol.color)

# If a class inherits from another with the same attributes or
# methods, it overrides them
