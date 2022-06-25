def par_ou_impar(num=0):
    if num % 2 == 0:
        return True
    else:
        return False


print('{:=^22}'.format(' Par Ou Impar '))
n = int(input('Digite um número: '))
print('É par!' if par_ou_impar(n) else 'É impar!')
