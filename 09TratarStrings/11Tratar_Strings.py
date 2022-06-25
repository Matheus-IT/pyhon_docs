"""
    join - joins a list of strings with another string as a separator.
    replace - replaces one substring in a string with another.
    startswith and endswith - determine if there is a substring at the start and end of a string, respectively.
    To change the case of a string, you can use lower and upper.
    The method split is the opposite of join, turning a string with a certain separator into a list.

    print(", ".join(["spam", "eggs", "ham"]))
    #prints "spam, eggs, ham"

    print("Hello ME".replace("ME", "world"))
    #prints "Hello world"

    print("This is a sentence.".startswith("This"))
    # prints "True"

    print("This is a sentence.".endswith("sentence."))
    # prints "True"

    print("This is a sentence.".upper())
    # prints "THIS IS A SENTENCE."

    print("AN ALL CAPS SENTENCE".lower())
    #prints "an all caps sentence"

    print("spam, eggs, ham".split(", "))
    #prints "['spam', 'eggs', 'ham']"
"""

frase = 'Curso Em Vídeo Python'
print(frase[6:14])#Começa do 6 termina no 14
print(frase[:5])#Do início até o 5
print(frase[15:])#Do 15 até o final
print(frase[::2])#Toda frase pulando de 2 em 2

print('''
Quando quiser escrever um texto de multiplas linhas em python basta coloca-lo em aspas triplas dentro de uma função
print, assim o texto será exibido integralmente com todos os espaços e quebras de linha. Podendo ser usado também pa-
ra a criação de menus interativos e economizando várias funções print para cada linha do texto
''')

print(frase.count('o'))#Mostra quantas vezes a letra 'o' se repete na frase
print(frase.upper())#Mostra a frase em letras maiúsculas
print(len(frase))#Função len diz qual o tamanho da frase
print(frase.strip())#Remove os espaços em branco no começo e no final
print(frase.replace('Python', 'Android'))#Troca a palavra Python por Android(Porém não salva o resultado)
frase = frase.replace('Python', 'Android')#Troca Python por Android e SALVA o resultado
print('Curso' in frase)#Retorna True ou False se tem a palavra Curso na frase
print(frase.find('Vídeo'))#Mostra em qual posição(primeira letra) está a palavra Vídeo
print(frase.split())#Divide as palavras da frase
dividido = frase.split()#Posso armazenar em uma variável
print(dividido[2])#A terceira palavra que foi dividida
print(dividido[2][3])#A quarta letra da terceira palavra
