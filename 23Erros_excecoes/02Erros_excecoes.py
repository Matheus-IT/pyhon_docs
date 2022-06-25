'''
Common exceptions:
ImportError: an import fails;
IndexError: a list is indexed with an out-of-range number;
NameError: an unknown variable is used;
SyntaxError: the code can't be parsed properly;
TypeError: a function is called on a value of an inappropriate type;
ValueError: a function is called on a value of the correct type, but with an inappropriate value.
'''
try:
    a = float(input('Numerador: '))
    b = float(input('Denominador: '))
    r = a / b
except (ValueError, TypeError): #Para mais de um tipo de exceção usar parênteses
    print('Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero')
except KeyboardInterrupt:
    print('O usuário preferiu não informar seus dados')
except Exception as erro: #Se for qualquer exceção não listada acima...
    print(f'Erro encontrado {erro.__cause__}')
else:
    print(f'Resultado divisao {r:4.2f}')
finally:
    print('Volte sempre muito obrigado')
