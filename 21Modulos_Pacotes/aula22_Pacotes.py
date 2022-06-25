from pacote_uteis import numeros #Importa o pacote 'numeros' que esta dentro do pacote 'pacote_uteis'


#Programa principal
n = int(input(' - Digite um numero: '))
print(f' - O numero e positivo: {numeros.e_positivo(n)}')
print(f' - {n} elevado ao quadrado = {numeros.quadrado(n)}')
print(f' - O dobro de {n} e {numeros.dobro(n)}')
print(f' - O triplo de {n} e {numeros.triplo(n)}')
