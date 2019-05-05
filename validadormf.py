count = 0
cont = 's'
while cont == "s":
    count += 1
    s = str(input('Digite um sexo [M/F]: ')).strip().upper()
    if s not in 'MF':
        count -= 1
        print('Você digitou um valor inválido, por favor, tente novamente!')
        print(s)
    cont = str(input('Deseja continuar? [S/N]'))
print('Você digitou {} sexos.'.format(count))
