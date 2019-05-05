n = int(input('Digite o primeiro valor: '))
raz = int(input('Digite a razão: '))
count = 0
mais = 10
total = 0
while mais != 0:
    mais += total
    while count <= mais:
        count += 1
        n += raz
        print(' {} ...'.format(n))
    print('PAUSA')
    total = int(input('Quantos numeros mais?'))
print('fim')