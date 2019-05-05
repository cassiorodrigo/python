from random import randint
c = 0
tupla = (randint(0, 999), randint(0, 999), randint(0, 999), randint(0, 999), randint(0, 999),)
#for c in range(0, 5):
#   c += 1
#if tupla[c] > tupla[c + 1] > tupla[c + 2] > tupla[c + 3] > tupla[5]:
a = sorted(tupla)
print(f'O maior número é: {a[4]}')
print(f'O menor número é: {a[0]}')
print(tupla)
