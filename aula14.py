s = str(input('Digite seu sexo [M/F] ')).strip().upper()[0]
while s not in 'MmFf':
    s = str(input('Entrada Invalida, por favor digite [M/F]: ')).strip().upper()[0]
print('Você digitou {}.'.format(s))

'''r = 'S'
while r == 'S':
    n = int(input('Digite um numero: '))
    r = str(input('Quer continuar: [S/N ')).upper()
print('FIM')'''