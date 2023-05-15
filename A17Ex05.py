num = []
par = []
imp = []
while True:
    num.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar? [S/N] '))
    while r not in 'SsNn':
        r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    else:
        imp.append(v)
print('--' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {imp}')