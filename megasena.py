from random import randint
from time import sleep
num = 0
qtos = int(input('Quantos jogos você quer gerar? \n'))
seq = list()
jogos = list()
count = 0
while count != qtos:
    for c in range(0, 6):
        num = randint(0, 60)
        if num not in seq:
            seq.append(num)
    seq.sort()
    jogos.append(seq[:])
    seq.clear()
    count += 1

print('='*40)
print('{:^40}'.format('JOGO DA MEGASENA'))
print('='*40)
for c in range(0, len(jogos)):
    print(f'Jogo número {c+1}: ', end='')
    print(jogos[c])
    sleep(0.75)
print('{:^40}'.format('>>>>>>>>>> Boa Sorte! <<<<<<<<<<'))