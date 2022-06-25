try:
    a = float(input('Numerador: '))
    b = float(input('Denominador: '))
    r = a / b
except Exception as erro: #'erro' será a exceção que for levantada
    print(f'Problema encontrado {erro.__class__}')
else: #Se não for levantada nenhuma exceção, mostra o resultado
    print(f'Resultado divisao {r:4.2f}')
finally: #O que estiver em finally vai ser execultado sempre
    print('Volte sempre muito obrigado')
