galera = list()
dado = list()
tot_mai = tot_men = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] > 21:
        print(f'{p[0]} é maior de idade')
        tot_mai += 1
    else:
        print(f'{p[0]} é menor de idade')
        tot_men += 1
print(f'Temos {tot_mai} maiores e {tot_men} menores')
