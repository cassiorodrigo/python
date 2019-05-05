v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
m1 = 0
while m1 != 5:
    m1 = int(input('''Escolha uma opção.
[1] Somar
[2] Multiplicar
[3] maior
[4] novos numeros
[5] Sair do Programa'''))
    if m1 == 1:
        print(v1 + v2)
    elif m1 == 2:
        print(v1 * v2)
    elif m1 == 3:
        if v1 > v2:
            print('{} é maior'.format(v1))
        elif v2 > v1:
            print('{} é maior'.format(v2))
        elif v2 == v1:
            print('Os numeros são iguais!')
    elif m1 == 4:
        v1 = int(input('Digite o primeiro valor: '))
        v2 = int(input('Digite o segundo valor: '))

print('FIM')
