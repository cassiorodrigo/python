n = int(input('Digite o termo inicial da PA: '))
raz = int(input('Digite a razão: '))
count = 0
opçao = 10
total = 0
while opçao != 0:
    total += opçao
    while count <= total:
        print('{} -- '.format(n), end='')
        n += raz
        count += 1
    print('Pausa')
    opçao = int(input('Quantos termos mais mostrar?'))
print('FIM')
#    res = n + raz
