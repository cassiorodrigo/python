'''tempo = int(input('Qual é o ano do seu carro?\n'))
if tempo <=3:
    print('Carro novo, hein!!!')
else:
    print('Quer andar de carro velho, amor, que venha!')
print('---FIM---')

import random
a = random.randINT(0,5)
guess = int(input('Advinhe o numero\n'))
if guess == a:
    print('Você acertou')
else:
    print('Você perdeu, o numero escolhido foi {}' .format(a))

velocidade = int(input('Velocidade registrada\n'))
qmulta = 80 - velocidade
multa = qmulta * -7.00
if velocidade > 80:
    print('Valor da multa esperado R${:.2f}'.format(multa))

n = int(input('Digite um numero\n'))
if n % 2 == 0:
    print('par')
else:
    print('impar')

n = int(input('Digite um numero\n'))
n2 = int(input('Digite um numero\n'))
n3 = int(input('Digite um numero\n'))
a = n/n2
b = n2/n3
c = n3/n

if a > c:
    print('O maior numero é {} \nO menor numero é {}'.format(n, n3))
else:
    print('nao sei')

from datetime import date
ano = int(input('Digite o ano que deseja analisar. \nSe quiser analisar o ano atual, digite 0\n'))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano é Bissexto')
else:
    print('O ano não é Bissexto')

a = int(input('Digite um Numero\n'))
b = int(input('Digite um Numero\n'))
c = int(input('Digite um Numero\n'))
maior = a
if c > b and c > a:
    maior = c

from time import sleep
a = int(input('Digite o tamanho do primeiro lado\n'))
b = int(input('Digite o tamanho do segundo lado\n'))
c = int(input('Digite o tamanho do terceiro lado\n'))
print('Analisando...')
sleep(3)
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
if maior > a + b + c - maior:
    print('Nao forma uma triangulo')
else:
    print('Forma um triangulo')
'''

