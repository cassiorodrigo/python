opçao = 's'
count = 0
soma = 0
menor = maior = int()
n = int()
comparador = int()
while opçao != 'n':
    count += 1
    comparador = n
    n = int(input('Digite um número: '))
    if count == 1:
        maior = menor = n
    else:
        if n < comparador:
            menor = n
        if n > comparador:
            maior = n

    soma += n

    opçao = str(input('para parar, pressione [n] e enter')).strip().lower()
med = soma / count

print('Você digitou {} números, sendo o maior {}, o menor {} e a média entre todos os numeros é {}'.format(count, maior, menor, med))