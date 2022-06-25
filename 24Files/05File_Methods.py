file1 = open('23Files/arquivo01.txt', 'r')
print(file1.read()) # Lendo o conteúdo do arquivo, posso colocar como parametro a quantidade de caracteres
print(file1.tell()) # Conta o número de caracteres
print(file1.seek(0, 0)) # Retorna para o início do arquivo

file1 = open('23Files/arquivo01.txt', 'w')
print(file1.write('Testando gravacao de arquivos em python')) # Grava no arquivo e retorna a quantidade de caracteres
file1.close()
