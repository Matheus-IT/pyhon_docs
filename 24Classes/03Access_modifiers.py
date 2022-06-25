'''Python doesn't have any mechanism that effectively restricts access to any instance
variable or method. Python prescribes a convention of prefixing the name of the variable/method
with single or double underscore to emulate the behaviour of protected and private
access specifiers: '''


class Caneta:
    def __init__(self): # Método construtor
        self.modelo = '' # Public attribute
        self.cor = ''
        self.__ponta = 0.0 # Private attribute
        self._carga = 0 # Protected attribute
        self._tampa = False
    
    def escrever(self):
        pass
    
    def rebiscar(self):
        pass


caneta1 = Caneta() #Instancia a classe ao objeto

print(caneta1.__ponta)
